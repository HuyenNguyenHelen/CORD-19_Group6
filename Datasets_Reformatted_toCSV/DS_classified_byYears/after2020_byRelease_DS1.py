# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)

before = []
after=[]

for id, abstr, year in zip(df['title'], df['abstract'], df['publish_time']):
    if re.search('2020', str(year)):
        after.append([id, abstr, year])
    else:
        before.append([id, abstr, year])

df_before = pd.DataFrame(before,columns=['title', 'abstract','publish_time'])
print(len(df_before)) #27453

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DS1\before2020.csv", "w", newline="",
          encoding='utf-8') as file:
    df_before.to_csv(file)

df_after = pd.DataFrame(after,columns=['title', 'abstract','publish_time'])
print(len(df_after)) #2047
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DS1\after2020.csv", "w", newline="",
          encoding='utf-8') as f:
    df_after.to_csv(f)








