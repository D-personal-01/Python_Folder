
#Q9. Accept words in a loop from the user. If a palindrome is entered (e.g., madam, 121), break the loop and display "Palindrome Detected. Stopping." Otherwise, keep appending the words to a list and print the final list at the end. (CO2) 


a = []

while 1:
    x = input("Enter word: ")

    if x == x[::-1]:
        print("Palindrome Detected. Stopping.")
        break
    else:
        a.append(x)

print("Final list:", a)