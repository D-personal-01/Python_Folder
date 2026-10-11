#Q10. Write a Python script to take 5 tuples as input from the user (each with 2 elements) and store them in a list. Then find the tuple with the highest second value. 

a=eval(input("Enter a tuple with 2 values:"))
b=eval(input("Enter a tuple with 2 values:"))
c=eval(input("Enter a tuple with 2 values:"))
d=eval(input("Enter a tuple with 2 values:"))
e=eval(input("Enter a tuple with 2 values:"))
l1=[a,b,c,d,e]
m=l1[0][1]
for i,j in l1:
    if m<j:
        m=j

print(m)
