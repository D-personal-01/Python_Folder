dict1={}
for i in range(1,11):
    dict1[i]=i**2
print(dict1)
for i in range(1,11):
    dict1.update({i:dict1[i]*i})
print(dict1)