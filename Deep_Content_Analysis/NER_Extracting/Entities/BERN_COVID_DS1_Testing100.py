import pandas as pd
import requests

def bern_ent_extraction(query):
    try:
        ent_info = query_raw(query)
        extracted_ents = extract_ents(ent_info)
        return extracted_ents
    except:
        return None


def query_raw(text, url="https://bern.korea.ac.kr/plain"):
    return requests.post(url, data={'sample_text': text}).json()


# define functions to extract ENTs from Bern model


# find_ent_index(ents)
def extract_ents(ents_info):
    index = find_ent_index(ents_info)
    extracted_ents = find_ent(index)
    return extracted_ents


def find_ent_index(ents_info):
    ent_index = {}
    for k, v in ents_info['logits'].items():
        if v:
            l = [v[0][0]["start"], v[0][0]["end"]]
            tup = tuple(l)
            ent_index[k] = tup
    return ent_index


def find_ent(ent_index):
    extracted_ent = {}
    for k, v in ent_index.items():
        extracted_ent[k] = query[v[0]:v[1]]
    return extracted_ent


with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_RelatedBody_sentSplit.csv", 'r', newline='', encoding='utf-8') as file:
    df = pd.read_csv(file)
for sent in df.sentence:
    query = sent
if __name__ == '__main__':
    query_raw(query)

bern_ents = []
sents_list=[]
for sent in df.sentence[:100]:
    sents_list.append(sent)
    query = sent
    bern_ents.append(bern_ent_extraction(query))

print(bern_ents)
#df['BERN_entities'] = bern_ents
df_ent = pd.DataFrame(list(zip(sents_list,bern_ents)), columns=["sentences", "BERN_entities"])
with open (r"E:\Helen\FinalProject_INFO5731\COVID_19_relatedWorking\All_COVID_related_body_sentSplited\COV_RelatedBody_sentSplit_testing.csv", 'w', newline='', encoding='utf-8') as file:
    df_ent.to_csv(file)