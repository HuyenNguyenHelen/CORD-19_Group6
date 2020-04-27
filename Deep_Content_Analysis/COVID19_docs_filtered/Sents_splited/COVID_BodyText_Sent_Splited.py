import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_DS\COVID19_AllRelated_bodyText_DS1.csv", 'r', newline='', encoding='utf-8') as file:
    df = pd.read_csv(file)
# split sentences
sent_dic={}
sentID = []
all_sents = []
for id, doc in zip(df.doc_ID, df.COVID19_related_bodytext):
    sents=[sent for sent in sent_tokenize(doc)]
    for sent in sents:
        all_sents.append(sent)
    for j in range(1, len(sents) + 1):
        sentID.append (str(id[2:int(len(id)-2)])+ "_sent_"+str(j))
#sent_dic[sentID] = sents

print(len(sentID))
print(len(all_sents))

df_sents = pd.DataFrame(list(zip(sentID, all_sents)),
               columns =['sentenceID', 'sentence'])
df_sents.head(100)
with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_RelatedBody_sentSplit.csv", 'w', newline='', encoding='utf-8') as file:
    df_sents.to_csv(file)