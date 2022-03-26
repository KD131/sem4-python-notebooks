import folium
import pandas as pd
import requests

url = "https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:monumenter&outputFormat=csv&SRSNAME=EPSG:4326"
url = "./monumenter.csv"    # easier to just use a local file, but getting by URL also works.

df = pd.read_csv(url)
# shows some data
print(df.head())


# 1. Hvor mange monumenter er der i København?
print("No. monuments:", len(df.index))

# 2. Hvor mange monumenter bliver vedligeholdt? Dvs. graffitirenhold = ja
mask_maintenance = df["graffitirenhold"] == "Ja"
print("No. being maintained:", sum(mask_maintenance))

# 3. Lav en funktion som kan finde koordinaterne på et monument baseret på monumentets id eller navn?
# 	F.eks:
# 		def monumentById(monumentId):
# 			return coordinates
def coordsById(id):
    """Returns coordinates as a tuple (x, y)"""
    # return df[df["id"] == id].iloc[0].loc[["x", "y"]] # returns as series, I think. Some weird number formatting going on though when I printed it.
    mon = df[df["id"] == id].iloc[0]
    return (mon["x"], mon["y"])

def latLonById(id):
    """Returns latitude and longitude as a tuple (lat, lon)"""
    mon = df[df["id"] == id].iloc[0]
    return (mon["latitude"], mon["longitude"])

id = 50058
coords = coordsById(id)
lat_lon = latLonById(id)
print(coords)
print(lat_lon)

# 3.a Vis monument som bliver returneret i metoden, på et kort over københavn ved brug af plotting.
#   (Se afsnittet om 'Folium and Bokeh' under notebooks/03-3 Plotting)
def get_city_location(city='Copenhagen'):
    """Get the location coordinates from OpenStreetMaps"""
    url_nomatim_api = 'https://nominatim.openstreetmap.org/search'
    r = requests.get(url_nomatim_api, params={'format': 'json', 'city': city})
    location = r.json()[0]  # Potentially many matches
    lat, lon = float(location['lat']), float(location['lon'])
    return lat, lon

cph_lat_lon = get_city_location()

def plotMonumentOnMap(lat_lon):
    """
    Creates a map and plots the monument on the map. Saves the map to file.

    Parameters
    ----------
    lat_lon : tuple
        Latitude and longitude (lat, lon)
    """
    m = folium.Map(location=cph_lat_lon, zoom_start=13)
    name = nameByLatLon(*lat_lon)
    folium.Marker(lat_lon, popup=name).add_to(m)
    m.save("./single_monument.html")

# 4. Find navnet på monumentet med x og y koordinaterne eller længde- og breddegraderne?
def nameByCoords(x, y):
    return df[(df["x"] == x) & (df["y"] == y)].iloc[0]["navn"]  # remember those parentheses when using multiple boolean masks

def nameByLatLon(lat, lon):
    return df[(df["latitude"] == lat) & (df["longitude"] == lon)].iloc[0]["navn"]  # remember those parentheses when using multiple boolean masks

print(nameByCoords(*coords))    # unpacks the tuple from #3
plotMonumentOnMap(lat_lon)      # The execution of 3.a because I wanted to use the getName function

# 5. Lav en metode der optegner alle monumenterne på kortet ved brug af plotting.
def plotAllMonumentsOnMap():
    m = folium.Map(location=cph_lat_lon, zoom_start=13)
    # iterrows and iterating a DataFrame in general is supposedly an anti-pattern, but I didn't know what else to do.
    for idx, row in df.iterrows():
        folium.Marker([row["latitude"], row["longitude"]], popup=row["navn"]).add_to(m)
    m.save("./all_monuments.html")

plotAllMonumentsOnMap()

# 6. Gør kortet interaktiv så navnet på monumenterne vises når man trykker på et plot.
# (Se afsnittet om 'Interactive plots with bokeh' under notebooks/03-3 Plotting)

# The maps are already interactive using popups in folium, but I haven't looked into bokeh and solved it using that.
