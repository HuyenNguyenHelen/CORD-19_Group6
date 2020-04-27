import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
with open (r"E:\Helen\FinalProject_INFO5731\COPY_DS_metadata\COVID19_related_docs_DS1.csv", 'r', newline='', encoding='utf-8') as file:
    df = pd.read_csv(file)

# create docID
docID = []
for i in range (1, len(df)+1):
    docID.append(["doc_"+str(i)])
df['docID'] = docID
print(df.head(2))
# split sentences
sent_dic={}
sentID = []
all_sents = []
for id, doc in zip(df.docID, df.COVID19_abstract):
    sents=[sent for sent in sent_tokenize(doc)]
    for sent in sents:
        all_sents.append(sent)
    for j in range(1, len(sents) + 1):
        sentID.append (str(id[0])+ "_sent_"+str(j))
#sent_dic[sentID] = sents

print(len(sentID))
print(len(all_sents))

df_sents = pd.DataFrame(list(zip(sentID, all_sents)),
               columns =['sentenceID', 'sentence'])
print(df_sents.head(100))
with open (r"E:\Helen\FinalProject_INFO5731\COPY_DS_metadata\COVID19_SplitedSents_DS1.csv", 'w', newline='', encoding='utf-8') as file:
    df_sents.to_csv(file)