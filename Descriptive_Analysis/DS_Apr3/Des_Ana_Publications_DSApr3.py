import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
stopwords = set(STOPWORDS)

#Open metadata file to extract content
with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_April3\metadata_Apr3.csv","r", newline='', encoding='utf-8')as file:
    df= pd.read_csv(file)
file.close()

# Journals counting
hist=dict()
for journal in df['journal'].dropna():
    hist[journal.strip()]=hist.get(journal.strip(),0)+1
#print(hist)

journals_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
journals_ranked=pd.DataFrame.from_dict (journals_sorted,orient = 'index', columns = ['count'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\Journals_frequency_DSApr3.csv", 'w',  newline="",
          encoding='utf-8') as file:
    journals_ranked.to_csv(file)
print(journals_ranked.head(20))

journals=[k for k, v in journals_sorted.items() if v > 130]
count =[v for k, v in journals_sorted.items() if v > 130]


fig = plt.figure(figsize=(15, 6))
sns.barplot(x=count, y = journals , palette= "RdBu_r")
plt.xlabel('Frequency')
plt.ylabel('Journals')
plt.title("Top Most Published Journals", fontsize=25)

fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\Top Most Published Journals_DSApr3.jpg", bbox_inches='tight', dpi=200)

plt.show()

# PUBLICATIONS TIMES - YEARS

# The number of those paper was published
import re
import seaborn as sns;

sns.set()
import matplotlib.pyplot as plt

dates = ''
for date in df['publish_time'].dropna():
    dates = dates + " " + str(date)

years = re.findall("(19\d{2})", dates)
years.extend(re.findall("(20\d{2})", dates))

hist = {}
for year in years:
    hist[year] = hist.get(year, 0) + 1

years_key_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[0])}
df_years = pd.DataFrame.from_dict(years_key_sorted, orient='index')

years_val_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
years_ranked = pd.DataFrame.from_dict(years_val_sorted, orient='index', columns=['quantity'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\Journals_overYears_DSApr3.csv", 'w',  newline="",
          encoding='utf-8') as file:
    years_ranked.to_csv(file)
print(years_ranked.head(10))
fig = plt.figure(figsize=(20, 6))
sns.set(style="whitegrid")
ax = sns.lineplot(hue="coherence", style="choice", palette=['blue'], linewidth=2.5,
                  markers=True, dashes=False, data=df_years)
plt.xticks(rotation=45,fontsize=7)
plt.ylabel('quantity')
plt.xlabel('years')
plt.title('The Number of Published Papers over Years', fontsize=30)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr3\Descriptive_analysis\Papers over Years_DSApr3.jpg", bbox_inches='tight', dpi=200)
plt.show()
