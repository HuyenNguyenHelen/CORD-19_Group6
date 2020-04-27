import pandas as pd
import csv
import spacy
import en_ner_bc5cdr_md
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher
import scispacy

# Apply scispacy model to recognize diseases and chemiscals
# This model referred to works of two authors in Kaggle: https://www.kaggle.com/maria17/cord-19-explore-drugs-being-developed


nlp = en_ner_bc5cdr_md.load()

# define models 
def scispacy_model(text, nlp):
    entities = {}
    doc = nlp(str(text.lower()))
    entities[doc.labels] = doc.ents
    return  entities #displacy.render(docs, style="ent", options=options),

text = 'The 2019–20 coronavirus pandemic is an ongoing pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)'

print(scispacy_model(text, nlp))