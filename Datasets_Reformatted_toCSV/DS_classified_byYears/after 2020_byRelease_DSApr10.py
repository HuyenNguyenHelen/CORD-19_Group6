# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_April10\metadata_Apr10.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)

before = []
after=[]

for id, abstr, year in zip(df['cord_uid'], df['abstract'], df['publish_time']):
    if re.search('2020', str(year)):
        after.append([id, abstr, year])
    else:
        before.append([id, abstr, year])

df_before = pd.DataFrame(before,columns=['cord_uid','abstract','publish_time'])
print(len(df_before)) #45748

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr10\before2020.csv", "w", newline="",
          encoding='utf-8') as file:
    df_before.to_csv(file)

df_after = pd.DataFrame(after,columns=['cord_uid', 'abstract','publish_time'])
print(len(df_after)) #5330
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr10\after2020.csv", "w", newline="",
          encoding='utf-8') as f:
    df_after.to_csv(f)








