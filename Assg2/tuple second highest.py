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
