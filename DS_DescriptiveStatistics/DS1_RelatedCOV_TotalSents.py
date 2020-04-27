
import pandas as pd
with open(r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_RelatedBody_sentSplit_DS1.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()
no_sents = len(df)
print(no_sents )
# total sentences DS1: 1129029