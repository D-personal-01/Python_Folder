#Q2. Given a list of student marks, write a Python program to find and display the second highest and second lowest marks using list operations. 

a=list(set(eval(input("Enter the list of marks:"))))

a=sorted(a)
print (a)
print("Second greatest:",a[-2])
print("Second lowest:",a[1])
