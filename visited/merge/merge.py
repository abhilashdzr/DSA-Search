import pandas as pd 

df1 = pd.read_csv("../codechef/codechef_no_title.csv")
df2 = pd.read_csv("../codeforces/codeforces_no_title.csv")
df3 = pd.read_csv("../leetcode/leetcode_no_title.csv")

print(df1.columns)
print(df2.columns)
print(df3.columns)

df = pd.concat([df1,df2,df3])
print(df.iloc[6336])
# df = df.drop(df.index[6336])
# print(df.iloc[6336])
# df.to_csv("/app/visited/merge/merged.csv",index=False)
# df = pd.read_csv("/app/visited/merge/merged.csv")
# print(df.iloc[6336]["Statement"])

# df = pd.read_csv("/app/visited/merge/merged3.csv")
# l = [i for i in range(len(df))]
# df.dropna()
# df.to_csv("/app/visited/merge/merged3.csv",index=False)


