import csv
import pandas as pd

# Dataset updated on April 3
with open (r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r", encoding = 'utf=8') as file:
    df=pd.read_csv(file)
count_Fulltext=0
count_all=0

for val in df['has_full_text']:
    if val:
        count_all +=1
    if val == True:
        count_Fulltext +=1
d={
   'have full-text': count_Fulltext,
   'total':count_all}


print(pd.DataFrame.from_dict (d, orient='index'))








