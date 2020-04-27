
import pandas as pd
import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)





# Open all csv files of DS1
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_biorxiv_medrxiv.csv", "r",  newline="", encoding='utf-8') as file:
    df1= pd.read_csv(file)
file.close()

df1['affiliations']=df1['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df1['affiliations']=df1['affiliations'].str.replace('[^\w\s,]','')
df1['affiliations']=df1['affiliations'].str.lower()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_comm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df2= pd.read_csv(file)
df2['affiliations']=df2['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df2['affiliations']=df2['affiliations'].str.replace('[^\w\s,]','')
df2['affiliations']=df2['affiliations'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_custom_license.csv", "r",  newline="", encoding='utf-8') as file:
    df3= pd.read_csv(file)
df3['affiliations']=df3['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df3['affiliations']=df3['affiliations'].str.replace('[^\w\s,]','')
df3['affiliations']=df3['affiliations'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr2_reformatted\reformatted_noncomm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df4= pd.read_csv(file)
df4['affiliations']=df4['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df4['affiliations']=df4['affiliations'].str.replace('[^\w\s,]','')
df4['affiliations']=df4['affiliations'].str.lower()
file.close()

# Create a string of institutions

affiliations = ''
for inst in df1['affiliations'].dropna():
    affiliations = affiliations + str(inst)
for inst in df2['affiliations'].dropna():
    affiliations = affiliations + str(inst)
for inst in df3['affiliations'].dropna():
    affiliations = affiliations + str(inst)
for inst in df4['affiliations'].dropna():
    affiliations = affiliations + str(inst)

# Set up paramaters for the wordcloud
wordcloud = WordCloud(width=1200, height=1000,
                      background_color='black',
                      stopwords=stopwords,
                      max_words=80,
                      max_font_size=100,
                      min_font_size=10).generate(affiliations)

# plot the wordcloud
fig=plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
title = "A WordCloud of Affiliations"
plt.title(title, fontdict={'size': 20, 'color': 'white',
                           'verticalalignment': 'bottom'})
plt.axis("off")
plt.tight_layout(pad=0)
fig.savefig("E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\institutions_wordcloud_DSApr3.jpg", bbox_inches='tight', dpi=200)
plt.show()

# Plot in top ones in barchart
import seaborn as sns

hist = dict()
for inst in affiliations.split(','):
    if len(inst.strip()) > 4:
        hist[inst.strip()] = hist.get(inst.strip(), 0) + 1

print(len(hist.keys()))
auth_inst_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
rank_affi = pd.DataFrame.from_dict(auth_inst_sorted, orient='index', columns=['count'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\institution_frequency_DSApr3.csv", 'w',  newline="",
          encoding='utf-8') as file:
    rank_affi.to_csv(file)

institutions = [k for k, v in auth_inst_sorted.items() if v >= 110]
frequency = [v for k, v in auth_inst_sorted.items() if v >= 110]

fig = plt.figure(figsize=(15, 6))
sns.barplot(x=frequency, y=institutions, palette='Blues_d')
plt.xticks(fontsize=7)
plt.xlabel('Frequency')
plt.ylabel('Institutions',fontsize=20)
plt.title("Top Affiliations", fontsize=20)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\Top_institutions_DSApr3.jpg", bbox_inches='tight', dpi=200)
plt.show()
