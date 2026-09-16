
#Q6. Take a string as input and perform the following operations: (CO2) 
#• Check if the string starts with a capital letter and ends with a punctuation mark 
#• Count the number of digits in the string 
#• Replace all spaces with dashes 
#• Convert the string to title case and print it 


str1 = input("Enter a string: ")

if str1[0].isupper() and str1[-1] in ''''.!?,;"':-''':
    print("Starts with capital letter and ends with punctuation mark")
else:
    print("Condition not satisfied")

count = 0

for x in str1:
    if x.isdigit():
        count = count + 1

print("Number of digits:", count)

str1 = str1.replace(" ", "-")
print("After replacing spaces:", str1)

str1 = str1.title()
print("Title case:", str1)