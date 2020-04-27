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

with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_related_SentsSplitted_Apr17\COV_RelatedBody_sentSplit_2-1.csv", 'r', newline='', encoding='utf-8') as file:
    df = pd.read_csv(file)

med_ents = []
#sents_list=[]
for sent in df.sentence:
    ents = med7_ents(sent)
    med_ents.append(ents)
    #sents_list.append(sent)


df['Med7_entities']=med_ents

with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_ENTS_extracted\MED7\Entities_Extracted_DSApr17-2-1.csv", 'w', newline='', encoding='utf-8') as file:
    df.to_csv(file)