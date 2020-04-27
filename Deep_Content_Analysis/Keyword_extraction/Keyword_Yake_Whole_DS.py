# APPLY YAKE MODEL
import pandas as pd
import matplotlib
import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import WordNetLemmatizer
import yake
stopwords = set(STOPWORDS)
lemmatizer = WordNetLemmatizer()
'''
with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df1= pd.read_csv(file)
file.close()

df1['abstract']=df1['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df1['abstract']=df1['abstract'].str.replace('[^\w\s,]','')
df1['abstract']=df1['abstract'].str.lower()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr3\after2020_newOnly_Ap3.csv", "r",  newline="", encoding='utf-8') as file:
    df2= pd.read_csv(file)
df2['abstract']=df2['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df2['abstract']=df2['abstract'].str.replace('[^\w\s,]','')
df2['abstract']=df2['abstract'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr10\after2020_newOnly_Apr10.csv", "r",  newline="", encoding='utf-8') as file:
    df3= pd.read_csv(file)
df3['abstract']=df3['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df3['abstract']=df3['abstract'].str.replace('[^\w\s,]','')
df3['abstract']=df3['abstract'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020_newOnly_Apr17.csv", "r",  newline="", encoding='utf-8') as file:
    df4= pd.read_csv(file)
df4['abstract']=df4['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df4['abstract']=df4['abstract'].str.replace('[^\w\s,]','')
df4['abstract']=df4['abstract'].str.lower()
file.close()



text=''
for abstr in df1['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w)) #p_stemmer.stem(w)

for abstr in df2['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w)) #p_stemmer.stem(w)


for abstr in df3['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w)) #p_stemmer.stem(w)

for abstr in df4['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w)) #p_stemmer.stem(w)


# convert type of data


#print(text)
language = "en"
max_ngram_size = 2
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords =40

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,  dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)
df_keywords = pd.DataFrame(keywords)

#with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\YAKEkeywords_All-DS_2gram.csv", 'w',  newline="",
#          encoding='utf-8') as file:
 #   df_keywords.to_csv(file)

'''

with open(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\YAKEkeywords_All-DS_2gram.csv", "r",
              newline="", encoding='utf-8') as file:
    df = pd.read_csv(file, names = ['key_word', 'score'])
file.close()
single_kw = ''
for kw in df['key_word']:
    for w in kw.split():
        single_kw = single_kw +' '+ str(w)

print(single_kw)
# plot the wordcloud

wordcloud = WordCloud(width=1600, height=1600,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=23).generate(single_kw)

fig = plt.figure(figsize=(6, 6), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\YAKE-keywords\YAKEkeywords_All-DS_2gram_Wordcloud.jpg", bbox_inches='tight', dpi=200)
plt.show()
