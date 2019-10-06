import pandas as pd
import numpy as np
import re
import csv

df = pd.read_csv('results_pct_20180508.csv', index_col = 0)
df.sort_values(by=['contest_name'], inplace = True)
df.sort_values(by=['county'], inplace = True)
print(df.iloc[1])

index = df.index
indexArr = [index[0]]
for i in index:
    indexArr.append(i)
#print(len(indexArr))
counties = [indexArr[0]]
for i in indexArr:
    if i not in counties:
        counties.append(i)

indexArr.sort() #sorted all 49607 counties
counties.sort() #sorted only 100 counties
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
for x in range(49607):
    if re.search("NC HOUSE", str(df.iloc[x,4])):
        temp = str(indexArr[x])
        if tmp3 == temp: #current county
            print(int(df.iloc[x,12]))
            print(str(df.iloc[x,4]))
            print("total")
            grandTotal[b] += int(df.iloc[x,12])
        
        if tmp3 != temp: #next county
            e.update({counties[b] : grandTotal[b]}) #final update
            b = b + 1
            tmp3 = str(counties[b])
            print(int(df.iloc[x,12]))
            print(str(df.iloc[x,4]))
            print("total")
            grandTotal[b] += int(df.iloc[x,12])

        if re.search("REP", str(df.iloc[x,6])): #repeat for rep setion
            temp2 = str(indexArr[x])
            
            if tmp2 == temp2:
                print(int(df.iloc[x,12]))
                print(str(df.iloc[x,4]))
                print("repub")
                total_votes[a] += int(df.iloc[x,12])
            else:
                d.update({counties[a] : total_votes[a]})
                a = a + 1
                tmp2 = str(counties[a])
                print(int(df.iloc[x,12]))
                print(str(df.iloc[x,4]))
                print("repub")
                total_votes[a] += int(df.iloc[x,12])




with open('output.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, d.keys())
    writer.writeheader()
    writer.writerow(d)
    writer.writerow(e)

csvfile.close()
