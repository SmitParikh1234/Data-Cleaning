import csv
import pandas as pd

df=pd.read_csv("final_stars.csv")

print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("new.csv")