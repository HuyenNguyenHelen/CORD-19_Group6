# Building model
import spacy
import en_core_med7_lg
med7 =en_core_med7_lg.load()

def med7_ents ( text):
    entities = {}
    doc = med7(text)
    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities

text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'
print(med7_ents ( text))
