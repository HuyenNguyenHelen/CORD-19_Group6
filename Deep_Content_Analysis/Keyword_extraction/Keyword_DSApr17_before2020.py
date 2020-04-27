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
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
stopwords = set(STOPWORDS)

# open metadata file and cleaning
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\before2020.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

df['abstract']=df['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df['abstract']=df['abstract'].str.replace('[^\w\s,]','')
df['abstract']=df['abstract'].str.lower()
# Create PorterStemmer
p_stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# convert type of data
text=''
for abstr in df['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w)) #p_stemmer.stem(w)

print(text)

language = "en"
max_ngram_size = 2
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 2000

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,  dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)
df_keywords = pd.DataFrame(keywords)

with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\YAKEkeywords_DSApr17_by2020.csv", 'w',  newline="",
          encoding='utf-8') as file:
    df_keywords.to_csv(file)

# plot the wordcloud

kw_str = ''
for kw in keywords:
    kw_str = kw_str + str(kw[0])
wordcloud = WordCloud(width=1600, height=1600,
                      background_color='pink',
                      stopwords=stopwords,
                      min_font_size=23).generate(kw_str)

fig = plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wordcloud)
title = "A WordCloud of Keywords"
plt.title(title, fontdict={'size': 20, 'color': 'black', 'verticalalignment': 'bottom'})
plt.axis("off")
plt.tight_layout(pad=0)

fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\keywords_Wordcloud_DSApr17_by2020.jpg", bbox_inches='tight', dpi=200)
plt.show()
