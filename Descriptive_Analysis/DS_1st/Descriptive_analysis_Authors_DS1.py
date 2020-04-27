# Analysis on Authors' attributes: names,

import pandas as pd
import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Open all csv files of DS1
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_1st_reformatted\reformatted_biorxiv_medrxiv.csv", "r",  newline="", encoding='utf-8') as file:
    df1= pd.read_csv(file)
file.close()

df1['authors_names']=df1['authors_names'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df1['authors_names']=df1['authors_names'].str.replace('[^\w\s,]','')
df1['authors_names']=df1['authors_names'].str.lower()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_1st_reformatted\reformatted_comm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df2= pd.read_csv(file)
df2['authors_names']=df2['authors_names'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df2['authors_names']=df2['authors_names'].str.replace('[^\w\s,]','')
df2['authors_names']=df2['authors_names'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_1st_reformatted\reformatted_noncomm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df3= pd.read_csv(file)
df3['authors_names']=df3['authors_names'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df3['authors_names']=df3['authors_names'].str.replace('[^\w\s,]','')
df3['authors_names']=df3['authors_names'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_1st_reformatted\reformatted_pmc_custom_license.csv", "r",  newline="", encoding='utf-8') as file:
    df4= pd.read_csv(file)
df4['authors_names']=df4['authors_names'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df4['authors_names']=df4['authors_names'].str.replace('[^\w\s,]','')
df4['authors_names']=df4['authors_names'].str.lower()
file.close()

# WORDCLOUD - AUTHORS'NAMES
stopwords = set(STOPWORDS)

# create a string of authors' names
names = ''
for val in df1.authors_names:
    names = names + str(val)
for val in df2.authors_names:
    names = names + str(val)
for val in df3.authors_names:
    names = names + str(val)
for val in df4.authors_names:
    names = names + str(val)


# set paramaters for the wordcloud
wordcloud = WordCloud(width=1200, height=1200,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(names)

# plot the wordcloud
fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
title="A WordCloud of Authors' Names"
plt.title(title, fontdict={'size': 20, 'color': 'black', 'verticalalignment': 'bottom'})
plt.axis("off")
plt.tight_layout(pad = 0)
#fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\authornames_DS1_Wordcloud.jpg", bbox_inches='tight', dpi=200)
plt.show()


# RANK AUTHOR NAME FREQUENCY

hist = dict()
for name in names.split(','):
    if name.strip() != ' ':
        hist[name.strip()] = hist.get(name.strip(), 0) + 1

# print(hist)
auth_name_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
# print(auth_name_sorted)
rank_names = pd.DataFrame.from_dict(auth_name_sorted, orient='index', columns=['names'])

with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\common_authorName.csv", 'w',  newline="",
          encoding='utf-8') as file:
    rank_names.to_csv(file)
auth_names = [k for k, v in auth_name_sorted.items() if len(k) > 7 and v > 15]
frequency = [v for k, v in auth_name_sorted.items() if len(k) > 7 and v > 15]

fig = plt.figure(figsize=(15, 6))
ax = fig.add_axes([0, 0, 1, 1])
ax.barh(auth_names, frequency, color="g")
plt.ylabel('Author names')
plt.xlabel('Count')
plt.title('Top Most Common Author Names', fontsize=25)
fig.savefig("E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\Top_authorname_DS1.jpg", bbox_inches='tight', dpi=200)
plt.show()