from asyncore import write
from fast_read_data import *
import time 


start = time.time()
# fast_read("/app/tf-idf/tfidf_dict.csv",rows,cols)
df = pd.read_csv("/app/tf-idf/tfidf_compiled.csv")
df = df[["X","Y","TF-IDF"]]
print(df.head())
df.to_csv("/app/tf-idf/tfidf.csv",index=False)
end = time.time()
print(end-start)

