import pandas
import glob2
filelist=glob2.glob("files/file*.txt")
print(filelist)
for file in filelist:
    df=pandas.read_csv(file)
    m=df.mean()
    # m=float(m) 
    print(m)