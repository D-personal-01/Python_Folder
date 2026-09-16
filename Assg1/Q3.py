#Q3.Write a Python program that accepts a list of 5 student marks and classifies them as: (CO1) 
#• Distinction: 75 and above 
#• First Class: 60–74 
#• Second Class: 50–59 
#• Fail: Below 50 
    
n = []

for i in range(5):
    x = int(input("Enter marks: "))
    n.append(x)

print("\nResult:")

for x in n:
    if x >= 75:
        print(x, "- Distinction")
    elif x >= 60:
        print(x, "- First Class")
    elif x >= 50:
        print(x, "- Second Class")
    else:
        print(x, "- Fail")