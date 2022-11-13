
emp=[]

with open(r'Employee_202211130858.csv','r') as file:
    for i in file:
        row=i.split(',')
        row[-1]=row[-1][:-1]
        emp.append(row)

# print(emp_dic)

pro_dic={}
with open(r'Project_202211130858.csv','r') as file:
    for i in file:
        row=i.split(',')
        row[-1]=row[-1][:-1]
        if row[0] in pro_dic:
            pro_dic[row[0]].add(row[1])
        else:
            pro_dic[row[0]]=set()
        
        
        
            

