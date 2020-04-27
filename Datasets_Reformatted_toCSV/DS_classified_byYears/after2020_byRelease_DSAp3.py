# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

# classify docs before and after 2020
'''
with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_April3\metadata_Apr3.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)

before = []
after=[]

for id, t, abstr, year in zip(df['cord_uid'], df['title'], df['abstract'], df['publish_time']):
    if re.search('2020', str(year)):
        after.append([id, t, abstr, year])
    else:
        before.append([id, t, abstr, year])

df_before = pd.DataFrame(before,columns=['cord_uid','title', 'abstract','publish_time'])
print(len(df_before)) #42973

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr3\before2020.csv", "w", newline="",
          encoding='utf-8') as file:
    df_before.to_csv(file)

df_after = pd.DataFrame(after,columns=['cord_uid','title', 'abstract','publish_time'])
print(len(df_after)) #4325
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr3\after2020.csv", "w", newline="",
          encoding='utf-8') as f:
    df_after.to_csv(f)


'''
# Filter docs which are overlapped
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DS1\after2020.csv", "r", newline="",
          encoding='utf-8') as f:
    data1 = pd.read_csv(f)
 
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr3\after2020.csv", "r", newline="",
         encoding='utf-8') as f:
   data2 = pd.read_csv(f)
   
newDoc = []
for doc in  data2['title']:
    if doc not in data1['title']:
        newDoc.append(doc)
print(len(newDoc)) #4325







