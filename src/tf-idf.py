from email.header import Header
from lib2to3.pgen2.token import NEWLINE
from operator import mod
from xml.dom.expatbuilder import FragmentBuilder
import pandas as pd
from requests import head  
import numpy as np

from helpers import *

#TF matrix
#go thru each mod statement
#make the TF matrix by counting freq of each keyword in the statement
#TF value = TF freq/number of keywords in statement

#IDF matrix
#IDF (keyword) = log10(tot no. of docs / tot. freqs of keyword in corpus )
#tf-idf[doc][keyword] = tf[doc][keyword] * idf[keyword]


'''Read mod statements and keywords'''
mod_statements = pd.read_csv("/app/tf-idf/mod_statements.csv")["Mod_statement"].tolist()
keywords = pd.read_csv("/app/tf-idf/keywords.csv")["Keyword"].tolist()

#define tf matrix
#rows = number of documents
rows = len(mod_statements)
#cols = number of keywords
cols = len(keywords)


'''Initialize the tf, tot_f and freq arrays'''
tf = np.zeros((np.int64(rows),np.int64(cols)))
tot_f = np.zeros(cols)
#init with zeros
freq = np.zeros((np.int64(rows),np.int64(cols)))
idf = np.zeros(cols)
tfidf = np.zeros((rows,cols))



'''Calculate frequencies of jth keyword in ith doc
and total frequency of jth keyword'''

# flag = 1
# i is the index of the statement
for i in range(len(mod_statements)):
    #the statement split up into words
    try:
        statement = mod_statements[i].split(" ")
    except:
        print(i)
        continue

    # count the total number of keywords and the abs freq of each key
    tot = len(statement)
    #j is the index of the keyword
    for j in range(len(keywords)):
        key = keywords[j]
        #freq of jth keyword in ith doc
        if key in statement:
            freq[i][j] = statement.count(key)
            tf[i][j] = freq[i][j]/tot
            my_write("/app/tf-idf/tf.csv",{"X":i,"Y":j,"Keyword":key,"TF":tf[i][j]})
            my_write("/app/tf-idf/freq.csv",{"X":i,"Y":j,"Keyword":key,"Freq":freq[i][j]})

            tot_f[j]+=freq[i][j]

for j in range(cols):
    my_write("/app/tf-idf/totfreq.csv",{"Y":j,"Keyword":keywords[j],"Tot Freq":tot_f[j]})
    if tot_f[j]>0:
        idf[j] = np.log10(cols/tot_f[j])
        my_write("/app/tf-idf/idf.csv",{"Y":j,"Keyword":keywords[j],"Tot Freq":tot_f[j],"IDF": idf[j]})

        for i in range(rows):
            tfidf[i][j] = tf[i][j] * idf[j]
            if tfidf[i][j]>0:
                my_write("/app/tf-idf/tfidf_compiled.csv",{"X":i,"Y":j,"Keyword":keywords[j],"TF":tf[i][j],"IDF":idf[j],"TF-IDF":tfidf[i][j]})

    else:
        print(j,keywords[j])

'''Read keywords and tot freq'''
# df1 = pd.read_csv("/app/tf-idf/keywords.csv")
# df2 = pd.read_csv("/app/tf-idf/totfreq2.csv")

# for i in range(len(df1)):
#     val2 = df2.iloc[i]
#     if val2["Tot Freq"]==0.0:
#         df1 = df1.drop(df1.index[i])

# df1.to_csv("/app/tf-idf/keywords2.csv",index=False)
    



# for j in range(len(idf)):
#     for i in range(rows):
#         tfidf[i][j] = tf[i][j] * idf[j]
#         if tfidf[i][j]>0:
#             my_write("/app/tf-idf/tfidf_dict.csv",{"X":i,"Y":j,"TF-IDF":tfidf[i][j]})



'''Read the tot freq arr'''
# df = pd.read_csv("/app/tf-idf/tot_freq_keys2.csv")
# tot_f[df["Y"].tolist()] = df["Tot Freq"].tolist()

# '''Check for zero freq keyword and remove it'''
# l=[]
# for j in range(len(df)):
#     if tot_f[j]==0:
#         l.append(j)

# print(l)


'''Read the freq csv'''
# ftable = pd.read_csv("/app/tf-idf/freq2.csv")

# '''Read the freq table'''
# x_arr = ftable["X"].tolist()
# y_arr = ftable["Y"].tolist()
# f_arr = ftable["Freq"].tolist()
# freq[x_arr,y_arr] = f_arr


'''Calculate the TF array'''
# for i in range(rows):
    # tot_keys = len(mod_statements[i])
    # for j in range(cols):
    #     if freq[i][j]>0:
    #         tf[i][j] = freq[i][j]/tot_keys
    #         my_write("/app/tf-idf/tf2.csv",{"X":i,"Y":j,"TF":tf[i][j]})


'''Read the tot_freq table'''
# df = pd.read_csv("/app/tf-idf/tot_freq_keys2.csv")
# for j in range(len(df)):
#     y = df.iloc[j]["Y"]
#     f = df.iloc[j]["Tot Freq"]
#     tot_f[y]=f


'''Read the tf table'''
# df = pd.read_csv("/app/tf-idf/tf.csv")
# for i in range(len(df)):
#     x = int(df.iloc[i]["X"])
#     y = int(df.iloc[i]["Y"])
#     f = df.iloc[i]["TF"]
#     print(x,y,f)
    # tf[x][y] = f


'''Initialize the idf and tfidf arrays'''
idf = np.zeros(cols)
tfidf = np.zeros((rows,cols))

'''Calculate the idf arrays'''

# for i in range(len(df)):



'''Read the idf array'''
# df = pd.read_csv("/app/tf-idf/idf.csv")
# for i in range(len(df)):
#     y = int(df.iloc[i]["Y"])
#     val = df.iloc[i]["IDF"]
#     print(y,val)
#     idf[y] = val



#TFIDF
# tot = len(keywords)
# for j in range(cols):
#     for i in range(rows):
#         tfidf[i][j] = tf[i][j] * idf[j]
#         if tfidf[i][j]>0:
#             my_write("/app/tf-idf/tfidf_dict.csv",{"X":i,"Y":j,"TF-IDF":tfidf[i][j]})


'''Read the TF-IDF data '''

# table = pd.read_csv("/app/tf-idf/tfidf_dict.csv")
# x_arr = table["X"]
# y_arr = table["Y"]
# f_arr = table["TF-IDF"]
# tfidf[x_arr,y_arr] = f_arr

# print(freq[0][0])

















# df_tfidf = pd.DataFrame(tfidf)
# df_tfidf.to_csv("/app/tf-idf/tfidf.csv",index=False)

# idf = [0]*cols
# #go thru each keyword
# for i in range(len(keywords)):
#     key = keywords[i]
#     #go thru all statements and calculate nt
#     nt = 0
#     #tot freq of ith keyword in corpus i.e. rows number of docs
#     for j in range(rows):
#         nt+=freq[j][i]

#     # idf[i]=rows/nt

#     if nt==0:
#         print("row,col",j,i)


# #tf*idf
# tfidf = [[0]*cols]*rows


# x=[]
# y=[]
# val = []

# # for i in range(rows):
# #     for j in range(cols):
# #         tfidf[i][j]=tf[i][j]*idf[j]
# #         if tfidf[i][j]!=0:
# #             x.append(i)
# #             y.append(j)
# #             val.append(tfidf[i][j])


# # df = pd.DataFrame([x,y,val],cols=["X","Y","TF-IDF"])
# # df.to_csv("/app/tf-idf/tf-idf.csv")

# # for i in range(10):
# #     print(tfidf[0][i])








