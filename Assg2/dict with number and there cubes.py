#Q8. Create a dictionary where the keys are integers from 1 to 10 and the values are their squares. Then, update the dictionary so that the values become their cubes. 

dict1={}
for i in range(1,11):
    dict1[i]=i**2
print(dict1)
for i in range(1,11):
    dict1.update({i:dict1[i]*i})
print(dict1)