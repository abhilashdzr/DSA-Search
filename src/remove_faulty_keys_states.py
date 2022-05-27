import pandas as pd


'''From keywords part and freqs'''

#remove from tot freq csv
df = pd.read_csv("/app/tf-idf/tot_freq_keys.csv")
# ind_to_be_dropped = [5, 659, 663, 1082, 1270, 4159, 4168, 5200, 6363, 8745, 9566, 9767, 10842, 11207, 12665, 13556, 13799, 14026, 14027, 14186, 16195, 16765, 16766, 17594, 19145, 20142, 22746, 23071, 23343]
ind_to_be_dropped = [13810]
print(df.iloc[13810])
df = df.drop(df.index[13810])
df.to_csv("/app/tf-idf/tot_freq_keys.csv")

# #remove from keywords csv
df = pd.read_csv("/app/tf-idf/keywords.csv")
print(df.iloc[13810])
df = df.drop(df.index[13810])
df.to_csv("/app/tf-idf/keywords.csv") 



'''From statements part'''

#remove from mod statements
# df = pd.read_csv("/app/tf-idf/mod_statements.csv",usecols=["Mod_statement"])
# print(df.loc[6336,"Mod_statement"])
# df = df.reset_index()
# print(df.head())
# df = df.drop(df.index[6336])
# df.to_csv("/app/tf-idf/mod_statements.csv",index=False)
# df = pd.read_csv("/app/tf-idf/mod_statements.csv")
# print(df.columns)
# print(df.iloc[6336])

#remove from merged csv
# df2 = pd.read_csv("/app/visited/merge/merged.csv",usecols=["Title","Statement","Link","Tag"])
# df2 = df2.drop(index=[6336])
# # df.drop_duplicates(keep="first",inplace=True)

# df2.to_csv("/app/visited/merge/merged.csv",index=False)
# df2 = pd.read_csv("/app/visited/merge/merged.csv")
# print(df2.iloc[6336])

# print(len(df),len(df2))
