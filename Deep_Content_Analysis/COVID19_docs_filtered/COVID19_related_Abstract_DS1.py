# Filter papers which are related to COVID-19
import pandas as pd
import csv
from rank_bm25 import BM25Okapi
import pandas as pd
import scispacy
import nltk

# open metadata file to process abstract
with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

#tokenized docs
corpus = [abstrt for abstrt in df['abstract']]
tokenized_corpus=[]
for abstract in df['abstract']:
    tokenized_corpus.append(str(abstract).lower().split(" "))
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
df['COVID-19-related scores']=doc_scores

# Navigate parameters to filter results
docs_scores={corpus[i]:doc_scores[i] for i in range(len(corpus)) }
sorted_docs_scores =  {k: v for k, v in sorted(docs_scores.items(), key=lambda item: item[1], reverse=True)}
docs_scores_0 = {k:v for k,v in sorted_docs_scores.items() if v==0}
df_sorted_docs_scores = pd.DataFrame.from_dict (sorted_docs_scores,orient = 'index', columns = ['scores']).tail(100)
df_docs_scores_0 = pd.DataFrame.from_dict (docs_scores_0,orient = 'index', columns = ['scores'])

# COVID-19 related docs

covid19_docs=[doc for doc in docs_scores.keys() if doc not in docs_scores_0.keys()]
## Notes: add one column in metadatafile for these attribute
df_covid19_docs = pd.DataFrame(covid19_docs, columns=['COVID19_abstract'])
#df['COVID-19-related docs'] = covid19_filterDoc(df['abstract'])


with open (r"E:\Helen\FinalProject_INFO5731\COPY_DS_metadata\COVID19_related_abstract_DS1.csv", 'w', newline='', encoding='utf-8') as file:
    df_covid19_docs.to_csv(file)
print(len(doc_scores))
print(len(corpus))
print(len(docs_scores.keys()))
print(len(covid19_docs))
# The number of unrelated papers
len(df_docs_scores_0)