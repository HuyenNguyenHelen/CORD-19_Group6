#From Haihua Chen to Everyone:  12:01 PM
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/13/2020 11:35 AM
# @Author  : Haihua
# @Contact : haihua.chen@unt.edu
# @File    : test_bern.py
# Software : PyCharm




import requests

def query_raw(text, url="https://bern.korea.ac.kr/plain"):
    return requests.post(url, data={'sample_text': text}).json()


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


query = "Autophagy maintains tumour growth through circulating arginine. Autophagy captures intracellular components and delivers them to lysosomes, where they are degraded and recycled to sustain metabolism and to enable survival during starvation1-5. Acute, whole-body deletion of the essential autophagy gene Atg7 in adult mice causes a systemic metabolic defect that manifests as starvation intolerance and gradual loss of white adipose tissue, liver glycogen and muscle mass1. Cancer cells also benefit from autophagy."
if __name__ == '__main__':
    query_raw(query)

bern_ents = bern_ent_extraction(query)
print(bern_ents)








