import pandas as pd
import numpy as np
import re
import csv

df = pd.read_csv('https://query.data.world/s/xxuvyisnx5y3saqqkd3gdgass5v6od', index_col = 0)

index = df.index
indexArr = [index[0]]
for i in index:
    indexArr.append(i)
#print(len(indexArr))
counties = [indexArr[0]]
for i in indexArr:
    if i not in counties:
        counties.append(i)

indexArr.sort()
counties.sort()
total_votes = [0] * 100
grandTotal = [0] * 100
a = 0
b = 0

d = {}
d = dict()
e = dict()

tmp2 = str(counties[0])
tmp3 = str(counties[0])
for x in range(49607):
    if re.search("NC HOUSE", str(df.iloc[x,4])):
        temp = str(indexArr[x])
        if tmp3 is temp:
            grandTotal[b] += int(df.iloc[x,12])
        if tmp3 is not temp:
            e.update({counties[b] : grandTotal[b]})
            b = b + 1
            tmp3 = str(counties[b])

            grandTotal[b] += int(df.iloc[x,12])
        if re.search("REP", str(df.iloc[x,6])):
            temp = str(indexArr[x])
            if tmp2 is temp:
                total_votes[a] += int(df.iloc[x,12])
            else:
                d.update({counties[a] : total_votes[a]})
                a = a + 1
                tmp2 = str(counties[a])

                total_votes[a] += int(df.iloc[x,12])




csv_columns = ['County', 'Republican total votes']
csv_file = "output.csv"
# try:
with open('output.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, d.keys())
    writer.writeheader()
    #for data in d:
    writer.writerow(d)
    writer.writerow(e)
# except IOError:
#     print("I/O error")

csvfile.close()
