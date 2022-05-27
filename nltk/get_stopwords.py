import nltk
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')
#search for these in words and remove those words

print("hehe")
l = stopwords.words('english')

df = pd.DataFrame(l,columns=['Word'])
print(df)


df.to_csv("/app/nltk/stopwords.csv")