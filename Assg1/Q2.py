#Q2. Write a program that accepts three integers from the user. Then evaluate and display results for: (CO1)
#• (a > b) and (b < c) 
#• a | b 
#• not (a == c) 
#• (a ^ c) & b 


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("(x > y) and (y < z) =", (x > y) and (y < z))
print("x | y =", x | y)
print("not (x == z) =", not (x == z))
print("(x ^ z) & y =", (x ^ z) & y)