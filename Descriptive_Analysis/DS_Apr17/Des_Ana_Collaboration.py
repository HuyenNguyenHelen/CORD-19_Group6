
# good graph
# selected v>10

import pandas as pd

import pandas as pd
import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt








# Open all csv files of DS1
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr17_reformatted\reformatted_biorxiv_medrxiv.csv", "r",  newline="", encoding='utf-8') as file:
    df1= pd.read_csv(file)
file.close()

df1['affiliations']=df1['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df1['affiliations']=df1['affiliations'].str.replace('[^\w\s,]','')
df1['affiliations']=df1['affiliations'].str.lower()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr17_reformatted\reformatted_comm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df2= pd.read_csv(file)
df2['affiliations']=df2['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df2['affiliations']=df2['affiliations'].str.replace('[^\w\s,]','')
df2['affiliations']=df2['affiliations'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr17_reformatted\reformatted_custom_license.csv", "r",  newline="", encoding='utf-8') as file:
    df3= pd.read_csv(file)
df3['affiliations']=df3['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df3['affiliations']=df3['affiliations'].str.replace('[^\w\s,]','')
df3['affiliations']=df3['affiliations'].str.lower()
file.close()

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_Apr17_reformatted\reformatted_oncomm_use_subset.csv", "r",  newline="", encoding='utf-8') as file:
    df4= pd.read_csv(file)
df4['affiliations']=df4['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df4['affiliations']=df4['affiliations'].str.replace('[^\w\s,]','')
df4['affiliations']=df4['affiliations'].str.lower()
file.close()

stopwords = set(STOPWORDS)

colla = []
for affi_list in df1['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df2['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df3['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df4['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])

collaboration = []
for affi_list in colla:
    if affi_list:
        i = affi_list[0]
        for j in affi_list[1:]:
            if i.strip() != j.strip():
                if i.strip() != None or j.strip() != None:
                    if len(i ) >5 and len(j ) >5:
                        l = [i.strip(), j.strip()]
                        tup = tuple(l)
                        collaboration.append(tuple(l))
                    else:
                        pass


print(len(collaboration))
df_collaboration =pd.DataFrame(collaboration, columns = ['x' ,'y'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr17\Descriptive_analysis\collaborations_list_DSApr17.csv", 'w',  newline="",
          encoding='utf-8') as file:
    df_collaboration.to_csv(file)

# Count number of collaborations
hist ={}
for tup in collaboration:
    for item in tup:
        hist[item ] =hist.get(item, 0 ) +1
# print(hist)
sorted_hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
# print(sorted_hist)
colla_ranked =pd.DataFrame.from_dict (sorted_hist ,orient = 'index', columns = ['Number of collaborations'])
#with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr17\Descriptive_analysis\collaborations_ranked_DSApr17.csv", 'w',  newline="",
#           encoding='utf-8') as file:
#    colla_ranked.to_csv(file)
colla_ranked_top = {k :v for k ,v in hist.items() if k!= '' and v >= 90}

# print(colla_ranked_top)


# PLOT COLLABORATION IN GRAPH
import networkx as nx

G = nx.Graph()

filtered_collaboration = []
obmitted = [ 'ku leuven','national institute of infectious diseases']
for tup in collaboration:
    if tup[0] in obmitted or tup[1] in obmitted:
        pass
    elif tup[0] in colla_ranked_top.keys() and tup[1] in colla_ranked_top.keys():
        filtered_collaboration.append(tup)
    pass
# print(filtered_collaboration )
nodes = []
for tup in filtered_collaboration:
    if tup[0] not in nodes:
        nodes.append(tup[0])
    if tup[1] not in nodes:
        nodes.append(tup[1])
print(nodes)

sizes = {}
for node in nodes:
    for item in hist.items():
        sizes[node] = int(hist[node]) * 10
size_list = [size for size in sizes.values()]

colors = {}
china = ['tsinghua university','chinese academy of sciences','fudan university','chinese academy of agricultural sciences','the chinese university of hong kong']
usa = ['the scripps research institute','kansas state university', 'columbia university', 'university of maryland','cornell university','university of california','university of pennsylvania','university of washington','national institutes of health','washington university school of medicine', 'harvard medical school', 'university of texasmedical branch',]
uk = ['imperial college london', 'university of oxford', 'university of cambridge',]
others = ['university of toronto','leiden university medical center','utrecht university','national institute of infectious diseases']
for node in nodes:
    if node in china:
        colors[node] = 'yellow'
    elif node in usa:
        colors[node] = 'green'
    elif node in uk:
        colors[node] = 'red'
    elif node in others:
        colors[node] = 'blue'
    else:
        colors[node] = 'pink'

colors_list = [color for color in colors.values()]

labels = {}
for node in nodes:
    for item in hist.items():
        if hist[node] > 90:
            labels[node] = str(node)
        else:
            labels[node] = ''

# print(nodes)
G.add_nodes_from(nodes)
G.add_edges_from(filtered_collaboration)
G.number_of_edges()
G.number_of_nodes()
# H = nx.DiGraph(G)
pos = nx.spring_layout(G, scale=8)
fig = plt.figure(figsize=(8, 8))
nx.draw(G, pos, node_size=size_list, node_color=colors_list, width=1, edge_cmap=plt.cm.Blues, with_labels=False)
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='red')

plt.axis('off')
plt.title('Collaboration Network', size=17)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_Apr17\Descriptive_analysis\Collaboration_network_DSApr17.jpg",
            bbox_inches='tight', dpi=350)
plt.show()

'''
# for saving just in case 
# good graph
# top most selected


# WORDCLOUD - AUTHORS'NAMES
stopwords = set(STOPWORDS)

colla = []
for affi_list in df1['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df2['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df3['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])
for affi_list in df4['affiliations'].dropna():
    colla.append([item for item in affi_list.split(",") if not None])

collaboration = []
for affi_list in colla:
    if affi_list:
        i = affi_list[0]
        for j in affi_list[1:]:
            if i.strip() != j.strip() and i.strip() != '':
                l = [i.strip(), j.strip()]
                tup = tuple(l)
                collaboration.append(tuple(l))
            else:
                pass

print(len(collaboration))
df_collaboration = pd.DataFrame(collaboration, columns=['x', 'y'])
# with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\collaborations_list_DS1.csv", 'w',  newline="",
#          encoding='utf-8') as file:
#    df_collaboration.to_csv(file)

# Count number of collaborations
hist = {}
for tup in collaboration:
    for item in tup:
        hist[item] = hist.get(item, 0) + 1
# print(hist)
sorted_hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
# print(sorted_hist)
colla_ranked = pd.DataFrame.from_dict(sorted_hist, orient='index', columns=['Number of collaborations'])
# with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\collaborations_ranked_DS1.csv", 'w',  newline="",
#         encoding='utf-8') as file:
#  colla_ranked.to_csv(file)
colla_ranked_top = {k: v for k, v in hist.items() if k != '' and v >= 35}

# print(colla_ranked_top)


# PLOT COLLABORATION IN GRAPH
import networkx as nx

G = nx.Graph()

filtered_collaboration = []
for tup in collaboration:
    if tup[0] in colla_ranked_top.keys() and tup[1] in colla_ranked_top.keys():
        filtered_collaboration.append(tup)
    pass
# print(filtered_collaboration )
nodes = []
for tup in filtered_collaboration:
    if tup[0] not in nodes:
        nodes.append(tup[0])
    if tup[1] not in nodes:
        nodes.append(tup[1])
print(nodes)

sizes = []
for v in colla_ranked_top.values():
    x = int(v) * 30
    sizes.append(x)

labels = {}
for node in nodes:
    labels[node] = str(node)

# print(nodes)
G.add_nodes_from(nodes)
G.add_edges_from(filtered_collaboration)
G.number_of_edges()
G.number_of_nodes()
# H = nx.DiGraph(G)
pos = nx.spring_layout(G, scale=8)

fig = plt.figure(figsize=(14, 14))
nx.draw(G, pos, node_size=sizes, node_color='red', width=2, edge_cmap=plt.cm.Blues, with_labels=False)
nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.axis('off')
plt.title('Colaboration Network', size=17)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\Collaboration_network_DS1.jpg",
            bbox_inches='tight', dpi=500)
plt.show()

'''
