# SP 1 - Monuments in Copenhagen
*by Holmerne (Anders, Nicklas, René, Peter)*

Datasæt: https://www.opendata.dk/city-of-copenhagen/monumenter

CSV: https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:monumenter&outputFormat=csv&SRSNAME=EPSG:4326

1. Hvor mange monumenter er der i København?

2. Hvor mange monumenter bliver vedligeholdt? Dvs. graffitirenhold = ja

3. Lav en funktion som kan finde koordinaterne på et monument baseret på monumentets id eller navn?
	F.eks:
		def monumentById(monumentId):
			return coordinates
	
3.a Vis monument som bliver returneret i metoden, på et kort over københavn ved brug af plotting. (Se afsnittet om 'Folium and Bokeh' under notebooks/03-3 Plotting)

4. Find navnet på monumentet med x og y koordinaterne eller længde- og breddegraderne?
	
	x = 724407.424966
	y = 6175719.798486
	
	MULTIPOINT ((12.555485308174104 55.69383926601615))

5. Lav en metode der optegner alle monumenterne på kortet ved brug af plotting.

6. Gør kortet interaktiv så navnet på monumenterne vises når man trykker på et plot. (Se afsnittet om 'Interactive plots with bokeh' under notebooks/03-3 Plotting)

# Status
1-5 solved. 6 half solved because the map already interactive through using Markers in Folium.

To run it, just execute the python file like so: `python cph_monuments.py`

The script will print various results of the exercises and also create two map files.

You can view the resulting maps by opening `single_monument.html` or `all_monuments.html`.
