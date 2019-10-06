import pandas as pd
import numpy as np
import re
import csv

df = pd.read_csv('results_pct_20180508.csv', index_col = 0)
df.sort_values(by=['county'], inplace = True)

index = df.index
indexArr = [index[0]]
for i in index:
    indexArr.append(i)

counties = [indexArr[0]]
for i in indexArr:
    if i not in counties:
        counties.append(i)

total_votes = [0]*100
grandTotal = [0]*100
a = 0 #repub iterator
b = 0 #total iterator

d = {}
d = dict()
e = {}
e = dict()

#intial county (ALAMANCE)
tmp2 = str(counties[0])
tmp3 = str(counties[0])
for x in range(35410):
    if re.search("NC HOUSE", str(df.iloc[x,4])):
        temp = str(indexArr[x])

        if tmp3 == temp: #current county
            grandTotal[b] += int(df.iloc[x,12])
        
        if tmp3 != temp: #next county
            e.update({counties[b] : grandTotal[b]}) #final update
            while str(counties[b]) != str(indexArr[x]):
                b = b + 1
                e.update({counties[b] : 0})
                
            tmp3 = str(counties[b])
            grandTotal[b] += int(df.iloc[x,12])

        if re.search("REP", str(df.iloc[x,6])): #repeat for rep setion
            temp2 = str(indexArr[x])
            
            if tmp2 == temp2:
                total_votes[a] += int(df.iloc[x,12])
            
            if tmp2 != temp2:
                d.update({counties[a] : total_votes[a]})
                while str(counties[a]) != str(indexArr[x]):
                    a = a + 1
                    d.update({counties[a] : 0})
                    
                tmp2 = str(counties[a])
                total_votes[a] += int(df.iloc[x,12])


with open('counties.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, d.keys())
    writer.writeheader()
    writer.writerow(d)
    writer.writerow(e)

csvfile.close()
