import pandas as pd

df = pd.read_csv("/app/visited/codechef/codechef.csv")
df.insert(3,"Tag",["CC"]*len(df),True)
df.to_csv("/app/visited/codechef/cc2.csv",index=False)