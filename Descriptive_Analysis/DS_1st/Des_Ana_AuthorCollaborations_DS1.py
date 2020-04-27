
# good graph
# selected v>10

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
df_collaboratio n =pd.DataFrame(collaboration, columns = ['x' ,'y'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\collaborations_list_DS1.csv", 'w',  newline="",
           encoding='utf-8') as file:
    df_collaboration.to_csv(file)

# Count number of collaborations
his t ={}
for tup in collaboration:
    for item in tup:
        hist[item ] =hist.get(item, 0 ) +1
# print(hist)
sorted_hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}
# print(sorted_hist)
colla_ranke d =pd.DataFrame.from_dict (sorted_hist ,orient = 'index', columns = ['Number of collaborations'])
with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\collaborations_ranked_DS1.csv", 'w',  newline="",
           encoding='utf-8') as file:
    colla_ranked.to_csv(file)
colla_ranked_top = {k :v for k ,v in hist.items() if k!= '' and v >= 15}

# print(colla_ranked_top)


# PLOT COLLABORATION IN GRAPH
import networkx as nx

G = nx.Graph()

filtered_collaboration = []
obmitted = ['academy of military medical sciences', 'jilin university',
            'military veterinary research institute of academy of military medical sciences']
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
        sizes[node] = int(hist[node]) * 20
size_list = [size for size in sizes.values()]

labels = {}
for node in nodes:
    for item in hist.items():
        if hist[node] > 55:
            labels[node] = str(node)
        else:
            labels[node] = ''

# print(nodes)
G.add_nodes_from(nodes)
G.add_edges_from(filtered_collaboration)
G.number_of_edges()
G.number_of_nodes()
# H = nx.DiGraph(G)
pos = nx.spring_layout(G, scale=16)

fig = plt.figure(figsize=(14, 14))
nx.draw(G, pos, node_size=size_list, node_color='red', width=2, edge_cmap=plt.cm.Blues, with_labels=False)
nx.draw_networkx_labels(G, pos, labels, font_size=13, font_color='blue')

plt.axis('off')
plt.title('Colaboration Network', size=17)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Descriptive_analysis\Collaboration_network_DS1.jpg",
            bbox_inches='tight', dpi=500)
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
