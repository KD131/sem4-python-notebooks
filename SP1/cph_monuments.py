import pandas as pd

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

coords = coordsById(50058)
print(coords)

# 4. Find navnet på monumentet med x og y koordinaterne eller længde- og breddegraderne?
def nameByCoords(x, y):
    return df[(df["x"] == x) & (df["y"] == y)].iloc[0]["navn"]  # remember those parentheses when using multiple boolean masks

print(nameByCoords(*coords))    # unpacks the tuple from #3
