import pandas as pd


dic={}
with open(r'SQL\1068\PRODUCTS.csv','r') as file:
    for i in file:
        temp=i[:-1].split(',')
        dic[temp[0]]=temp[1]
res=[]
with open(r'SQL\1068\SALES.csv','r') as file:
    for i in file:
        temp=i[:-1].split(',')[1:]
        temp[0]=dic[temp[0]]
        r=''
        for i in temp:
            r+=i+','
        r=r[:-1]
        res.append(r)
with open('SQL\\1068\\res.csv','w')as file:
    for i in res:
        file.write(i)
        file.write('\n')