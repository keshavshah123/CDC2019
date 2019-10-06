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
text = "US HOUSE OF REPRESNTATIVES DISTRICT"
a = 0

tmp2 = str(counties[0])
for x in range(49607):
    if re.search("^US", str(df.iloc[x,4])):
        if re.search("REP", str(df.iloc[x,6])):
            temp = str(indexArr[x])
            #print(a)
            if re.search(str(tmp2), str(temp)):
                total_votes[a] += int(df.iloc[x,12])
            else:
                a = a + 1
                tmp2 = str(counties[a])
                total_votes[a] += int(df.iloc[x,12])



with open('output.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    for i in range(100):
        writer.writerow(str(counties[i]))

writeFile.close()
print(*total_votes)
