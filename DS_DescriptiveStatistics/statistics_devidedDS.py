# descriptive statistics

# DS before 2020
statistics = {}

import pandas as pd

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DS1\before2020.csv", "r", newline="",
          encoding='utf-8') as file:
    df1 = pd.read_csv(file)

count1 = 0
for data in df1['has_full_text']:
    if data == True:
        count1 += 1
print(count1)
len1 = len(df1)

# statistics ["Papers published before 2020 "] = len(df)
# print(statistics)

# 1 RELEASE - NEW ONLY


with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DS1\after2020.csv", "r", newline="",
          encoding='utf-8') as file:
    df2 = pd.read_csv(file)

count2 = 0
for data in df2['has_full_text']:
    if data == True:
        count2 += 1
print(count2)
len2 = len(df2)

# RELEASE 2 New only
count3 = 0
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr3\after2020_newOnly.csv", "r",
          newline="", encoding='utf-8') as file:
    df3 = pd.read_csv(file)

for val1, val2 in zip(df3['has_pdf_parse'], df3['has_pmc_xml_parse']):
    if val1 == True or val2 == True:
        count3 += 1
len3 = len(df3)
print(count3)

# RELEASE 3 New only
count4 = 0
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr10\after2020_newOnly.csv", "r",
          newline="", encoding='utf-8') as file:
    df4 = pd.read_csv(file)

for val1, val2 in zip(df4['has_pdf_parse'], df4['has_pmc_xml_parse']):
    if val1 == True or val2 == True:
        count4 += 1
len4 = len(df4)
print(count4)

# RELEASE 4 New only
count5 = 0
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020_newOnly.csv", "r",
          newline="", encoding='utf-8') as file:
    df5 = pd.read_csv(file)

for val1, val2 in zip(df5['has_pdf_parse'], df5['has_pmc_xml_parse']):
    if val1 == True or val2 == True:
        count5 += 1
len5 = len(df5)
print(count5)
dta_ = {
    'Data subset': ['Published before 2020', ' Published after 2020 until March 13', ' Published after 2020 until Apr3',
                    ' Published after 2020 until Apr10', ' Published after 2020 until Apr17'],
    'Total': [len1, len2, len3, len4, len5], 'Has full text': [count1, count2, count3, count4, count5]}
statDF = pd.DataFrame(dta_)

with open("E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\metadata_Old-NewOnly.xlsx", 'w', newline='',
          encoding='utf-8') as file:
    statDF.to_csv(file)

statDF








