from curses.ascii import isascii
from enum import unique
import pandas as pd

#load dataset
df = pd.read_csv("/app/visited/merge/merged.csv")
statements = df["Statement"]

# #load stopwords
stopwords=pd.read_csv("/app/nltk/stopwords.csv")["Word"].tolist()

#load stop keys
stop = [chr(92),"~","`",".","=","'",";","%","@","|","$","?","≠","->","≤","^","⊕","#","\leq","→","{","}","&","_","+","-","!","∑","[","]","/","<",">",":","(",")","*"]

remove = [".",",",":","\"","!","'","?","Tags","\t","\b"]

#unique keywords set
unique_words = set()

#remove the word if it has a digit in it
def has_number(word):
    for w in word:
        if ord(w)>=48 and ord(w)<=57:
            return True

    return False

def notEnglish(ch):
    if isascii(ch):
        return False
    else:
        return True


# #go thru each statement
df2 = []
for s in statements:
    # ind = df.index[df['Statement'] == s].tolist()[0]

    #remove some punctuation marks 
    for r in remove:
        s = s.replace(r,"")

    pruned_s = []

    #split the sentence into words
    words = s.split(" ")

    #go thru each word
    for word in words:
        #if word is a letter, leave it
        if(len(word)==1 or len(word)==0 ):
            continue

        word = word.lower()           
        flag = 1  #remains 1 if none of the stopwords present in word
        #word is a stopword
        if word in stopwords:
            flag=-1

        if has_number(word):
            flag=-1

        #go thru the word and find a stopkey
        for l in word:
            if l in stop or notEnglish(l):
                flag=-1
                break

        if flag==-1:
            continue

        pruned_s.append(word)

    unique_words = set(pruned_s).union(unique_words)
    
    mod_statement = ""
    for u in pruned_s:
        mod_statement+=u+" "


    df2.append(mod_statement.strip())


df2 = pd.DataFrame(df2,columns=["Mod_statement"])
df2.to_csv("/app/tf-idf/mod_statements.csv",index=False)

print(len(statements)==len(df2))


list_of_keywords = list(unique_words)
list_of_keywords.sort()
df3 = pd.DataFrame(list_of_keywords,columns = ["Keyword"])
df3.to_csv("/app/tf-idf/keywords.csv",index=False)


