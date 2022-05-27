import pandas as pd

df = pd.read_csv("/app/visited/merge/merged.csv")
df.drop_duplicates(keep="first",inplace=True)
df.to_csv("/app/visited/merge/merged.csv",index=False)
print(df[df.duplicated()])
