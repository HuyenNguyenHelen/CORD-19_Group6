# APPLY YAKE MODEL
import csv
import pandas as pd
import pandas as pd
import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import yake
import nltk
# nltk.download('wordnet')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

stopwords = set(STOPWORDS)

# open metadata file and cleaning
with open(r'E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020_newOnly_Apr17.csv', "r",
          newline="", encoding='utf-8') as file:
    df = pd.read_csv(file)
file.close()

df['abstract'] = df['abstract'].apply(
    lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df['abstract'] = df['abstract'].str.replace('[^\w\s,]', '')
df['abstract'] = df['abstract'].str.lower()
# Create PorterStemmer
p_stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


# convert type of data

def kw_extractor(text):
    language = "en"
    max_ngram_size = 2
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords,
                                                features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    return keywords


docID = []
for i in range(1, len(df) + 1):
    docID.append("Sub5_doc" + str(i))
df['docID'] = docID

all_keywords = {}
for id, abstr in zip(df['docID'], df['abstract']):
    if len(abstr) > 3:
        text = ''
        for w in abstr.split():
            if w not in stopwords:
                text = text + ' ' + str(lemmatizer.lemmatize(w))
        kw = kw_extractor(text)
        if kw:
            w = []
            for tup in kw:
                if float(tup[1]) > 0.008:
                    w.append(tup[0])
        all_keywords[id] = w

print(all_keywords)

df_keywords = pd.DataFrame.from_dict(all_keywords, orient='index')

with open(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\YAKEonDoc_after2020_DS1.csv", 'w', newline="",
          encoding='utf-8') as file:
    df_keywords.to_csv(file)
