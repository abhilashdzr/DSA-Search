import pandas as pd

from helpers import my_write

df = pd.read_csv("../visited/merge/merged.csv")
titles = df["Title"]
statements = df["Statement"]

for i in range(len(df)):
  t = titles.iloc[i]+" "
  s = statements.iloc[i]
  s = s.replace(t,"")
  s = s.replace('\\',"")
  print(t)

  my_dict = {"Title":t,"Statement":s,"Link":df["Link"].iloc[i],"Tag":df["Tag"].iloc[i]}
  my_write("../visited/merge/merged_no_titles.csv",my_dict)
  