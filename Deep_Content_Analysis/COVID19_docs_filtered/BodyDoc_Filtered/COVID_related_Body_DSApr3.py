# Filter papers which are related to COVID-19
import pandas as pd
import csv
from rank_bm25 import BM25Okapi
import pandas as pd
import scispacy
import nltk

# Open reformatted files for filtering
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_biorxiv_medrxiv.csv", "r",  newline="", encoding='utf-8') as file:
    df1= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_comm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df2= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_custom_license.csv", "r",  newline="", encoding='utf-8') as file:
    df3= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_noncomm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df4= pd.read_csv(file)
file.close()

#tokenized docs
corpus = []
for txt in df1['text']:
    corpus.append (txt)
for txt in df2['text']:
    corpus.append (txt)
for txt in df3['text']:
    corpus.append (txt)
for txt in df4['text']:
    corpus.append(txt)

tokenized_corpus=[]
for txt in corpus:
    tokenized_corpus.append(str(txt).lower().split(" "))
#print( tokenized_corpus)

bm25 = BM25Okapi(tokenized_corpus)

# search covid19_names as query
covid19_names = 'COVID-19 (COVID-19) COVID19 Coronavirus Corona SARS-CoV-2 2019-nCoV (2019-nCoV) (SARS-CoV-2) pandemic' # according WHO naming Covid-19
tokenized_covid19_names= covid19_names.lower().split(" ")

doc_scores = bm25.get_scores(tokenized_covid19_names)
#print(doc_scores)
bm25.get_top_n(tokenized_covid19_names, corpus, n=100)
#rank_doc_scores = enumerate(sorted(doc_scores), 1)
# Add column Scores to df
#df['COVID-19-related scores']=doc_scores

# Navigate parameters to filter results
docs_scores={corpus[i]:doc_scores[i] for i in range(len(corpus)) }
sorted_docs_scores =  {k: v for k, v in sorted(docs_scores.items(), key=lambda item: item[1], reverse=True)}
docs_scores_0 = {k:v for k,v in sorted_docs_scores.items() if v==0}
df_sorted_docs_scores = pd.DataFrame.from_dict (sorted_docs_scores,orient = 'index', columns = ['scores']).tail(100)
df_docs_scores_0 = pd.DataFrame.from_dict (docs_scores_0,orient = 'index', columns = ['scores'])

# COVID-19 related docs

covid19_docs=[doc for doc in docs_scores.keys() if doc not in docs_scores_0.keys()]

# create docID
docID = []
for i in range (1, len(covid19_docs)+1):
    docID.append(["doc_"+str(i)])
# Store in a csv file
df_covid19_docs = pd.DataFrame(list(zip(docID, covid19_docs)), columns=['doc_ID', 'COVID19_related_bodytext'])

with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_DS\COVID19_AllRelated_bodyText_DSApr3.csv", 'w', newline='', encoding='utf-8') as file:
    df_covid19_docs.to_csv(file)
print(len(doc_scores))
print(len(corpus))
print(len(docs_scores.keys()))
print(len(covid19_docs))
# The number of unrelated papers
len(df_docs_scores_0)