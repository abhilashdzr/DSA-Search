import pandas as pd

file1 = "/app/tf-idf/tot_freq_keys.csv"
file2 = "/app/tf-idf/keywords.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

print(len(df1))
print(len(df2))
print(df1.iloc[13810])
print(df2.iloc[13810])