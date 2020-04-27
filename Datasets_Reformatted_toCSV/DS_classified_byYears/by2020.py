# classify by the year of publication, after and before Dec2020

import pandas as pd
import re

# classify by the year of publication, after and before Dec2020

import pandas as pd
import re


with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_Apr17\metadata_Apr17.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)

before = []
after=[]

for id, t, abstr, year, pdf, pmc  in zip(df['cord_uid'],  df['title'], df['abstract'], df['publish_time'], df['has_pdf_parse'], df['has_pmc_xml_parse']):
    if re.search('2020', str(year)):
        after.append([id,t, abstr, year, pdf, pmc])
    else:
        before.append([id, t, abstr, year, pdf, pmc])

df_before = pd.DataFrame(before,columns=['cord_uid', 'title', 'abstract','publish_time', 'has_pdf_parse','has_pmc_xml_parse' ])
print(len(df_before)) #45748

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\before2020.csv", "w", newline="",
          encoding='utf-8') as file:
    df_before.to_csv(file)

df_after = pd.DataFrame(after,columns=['cord_uid', 'title', 'abstract','publish_time', 'has_pdf_parse','has_pmc_xml_parse'])
print(len(df_after)) #5330
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020.csv", "w", newline="",
          encoding='utf-8') as f:
    df_after.to_csv(f)








