import simplekml
import pandas

df=pandas.read_csv("files/coordinates.csv")
kml=simplekml.Kml()
for lon,lat in zip(df["Longitude"],df["Latitude"]):
    kml.newpoint(coords=[(lon,lat)])
kml.save("C:/Users/Win7/Downloads/Earth/Points.kml")    