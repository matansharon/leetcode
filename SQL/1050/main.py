import pandas as pd

# class Couple:
#     def __init__(self) -> None:
#         self.couple=()
#         self.timestamp=set()

df=pd.read_csv(r'act-dir.csv')
s=set()
dic={}
for i in df.itertuples():
    r=''
    r+=str(i[1])+str(i[2])
    if r in dic:
        dic[r].add(i[3])
    else:
        dic[r]=set()
        dic[r].add(i[3])
for i in dic:
    if len(dic[i])>2:
        print (i,dic[i])


