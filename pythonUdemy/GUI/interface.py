import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename
def browse():
    global infile
    infile=askopenfilename()
    

def kml_function(outfile="C:/Users/Win7/Downloads/Earth/Points.kml"):
    df=pandas.read_csv(infile)
    kml=simplekml.Kml()
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
    kml.save(outfile)  
root=tkinter.Tk() 
root.title("IVANA") 
label=tkinter.Label(root,text="This program generates a KML file")
label.pack()
browse_button=tkinter.Button(root,text="Browse",command=browse)
browse_button.pack()
kml_button=tkinter.Button(root,text="Generate KML",command=kml_function)
kml_button.pack()
root.mainloop()