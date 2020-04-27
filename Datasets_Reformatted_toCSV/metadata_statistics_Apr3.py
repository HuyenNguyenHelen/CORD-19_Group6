import csv
import pandas as pd

# Dataset updated on April 3
with open (r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_April3\metadata_Apr3.csv", "r", encoding = 'utf=8') as file:
    df=pd.read_csv(file)
count_both=0
count_PMC=0
count_PDF=0
count_None=0
for val1, val2 in zip(df['has_pdf_parse'], df['has_pmc_xml_parse']):
    if val1 == True and val2==True:
        count_both+=1
    elif val1 == False and val2==True:
        count_PMC+=1
    elif val1 == True and val2 == False:
        count_PDF+=1
    else:
        count_None+=1
total= count_both+count_PMC+count_PDF+count_None
d={'have both pdf and PMC full-text': count_both,
   'have only PMC full-text': count_PMC,
   'have only PDF full-text': count_PDF,
   'do not have full-text':count_None,
   'total':total}

print(pd.DataFrame.from_dict (d, orient='index'))








