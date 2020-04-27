# Testing model on 100 docs in DS1
import spacy
import pandas as pd
import en_core_med7_lg
med7 =en_core_med7_lg.load()

def med7_ents ( text):
    entities = {}
    doc = med7(text)
    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities

with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_RelatedBody_sentSplit_DS1.csv", 'r', newline='', encoding='utf-8') as file:
    df = pd.read_csv(file)

med_ents = []
#sents_list=[]
for sent in df.sentence[:100]:
    ents = med7_ents(sent)
    med_ents.append(ents)
    #sents_list.append(sent)


with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_ENTS_extracted\COV_RelatedBody_sentSplit_testing.csv", 'r', newline='', encoding='utf-8') as file:
    df_ent=pd.read_csv(file)

df_ent['Med7_entities']=med_ents

with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_ENTS_extracted\COV_RelatedBody_sentSplit_testing.csv", 'w', newline='', encoding='utf-8') as file:
    df_ent.to_csv(file)