
#Q1.Write a Python program that takes a list of user-defined variable names and checks which ones are Python reserved keywords.


import keyword

a = []
n=int(input("Enter the number of variable names: "))
for i in range(n):
    a.append(input("Enter the variable name: "))
for x in a:
    if keyword.iskeyword(x):
        print(x, "is a reserved keyword")
    else:
        print(x, "is not a reserved keyword")