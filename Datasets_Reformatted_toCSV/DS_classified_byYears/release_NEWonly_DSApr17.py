# Filter docs which are overlapped
with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr10\after2020.csv", "r", newline="",
          encoding='utf-8') as f:
    data1 = pd.read_csv(f)

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020.csv", "r", newline="",
          encoding='utf-8') as f:
    data2 = pd.read_csv(f)
oldDoc = [doc for doc in data1["cord_uid"]]
newDoc = []
for id, t, a in zip(data2["cord_uid"], data2['title'], data2['abstract']):
    if id not in oldDoc:
        newDoc.append([id, t, a])
print(len(newDoc))  # 2603
df_newOnly = pd.DataFrame(newDoc, columns=["cord_uid", 'title', 'abstract'])

with open(r"E:\Helen\FinalProject_INFO5731\CSV_formatted\DS_dividedbyYears\DSApr17\after2020_newOnly.csv", "w",
          newline="",
          encoding='utf-8') as f:
    df_newOnly.to_csv(f)
