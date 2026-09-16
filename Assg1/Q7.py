
#Q7. Accept a string from the user. Separate and print all the digits, alphabets, and special characters in the string in separate lines

str1=input("Enter the string: ")
digit=[]
alphabet=[]
special=[]
for i in range(len(str1)):
  if str1[i].isdigit():
    digit.append(str1[i])
  elif str1[i].isalpha():
    alphabet.append(str1[i])
  else:
    special.append(str1[i])
print("Digits are: ",digit)
print("Alphabets are: ",alphabet)
print("Special characters are: ",special)