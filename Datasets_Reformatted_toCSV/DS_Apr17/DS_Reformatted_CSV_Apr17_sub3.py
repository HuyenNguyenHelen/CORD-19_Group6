# Extract tarfile
# Import packages
import os
import json
import pandas as pd
import tarfile
'''
my_tar = tarfile.open("E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_Apr17\custom_license.tar.gz")
my_tar.extractall("E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_Apr17\DS_extracted")  # specify which folder to extract to
my_tar.close()
'''

# These codes for extracting content from pdf_json files in each subset.
# Notes: These codes are not for extracting content from pmc_json file in each subset

# Iterate to open and read all json files in folder
#first dir



dir1 = "E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_Apr17\DS_extracted\custom_license\pdf_json"
filenames1 = os.listdir(dir1)
print("Number of articles retrieved from :", len(filenames1))

dir2 = "E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_Apr17\DS_extracted\custom_license\pmc_json"
filenames2 = os.listdir(dir2)
print("Number of articles retrieved from :", len(filenames1))
# Store content of all json files from two dirs in a list
all_files = []
for filename in filenames1:
    filename = os.path.join(dir1, filename)  # 'r' +'"'+ os.path.join(biorxiv_dir, filename) + '"'
    filename.encode('unicode-escape')
    file = json.load(open(filename, 'rb'))
    all_files.append(file)

for filename in filenames2:
    filename = os.path.join(dir2, filename)  # 'r' +'"'+ os.path.join(biorxiv_dir, filename) + '"'
    filename.encode('unicode-escape')
    file = json.load(open(filename, 'rb'))
    all_files.append(file)

# What keys in those json files?
#print(all_files[800].keys())

# Extract all needed content

# Extract paperids and paper titles
paper_id = [file['paper_id'] for file in all_files]
titles = [file['metadata']['title'] for file in all_files]

# Extract author_names, affiliations, abstract_text, body_text

author_names, affiliations, body_text = [], [], []

authors = [file['metadata']['authors'] for file in all_files]
for element in authors:
    author_names.append([item['first'] + " " + item['last'] for item in element])
    try:
        affiliations.append([item['affiliation']['institution'] for item in element])
    except:
        affiliations.append(None)

bodies = [file["body_text"] for file in all_files]
for body in bodies:
    text = [para['text'] for para in body]
    body_text.append(text)

formated_data = {'paper_id': paper_id, 'title': titles, 'authors_names': author_names, 'affiliations': affiliations,
                  'text': body_text}

df = pd.DataFrame.from_dict(formated_data, orient='columns')
with open(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr17\reformatted_custom_license.csv", "w", newline="",
          encoding='utf-8') as file:
    df.to_csv(file)
df
