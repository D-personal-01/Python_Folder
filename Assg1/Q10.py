
#Q10. Create a number guessing game where: 
#• A random number is generated between 1 and 100 
#• The user gets a maximum of 7 attempts to guess the number 
#• For each wrong guess, give a hint – “Too High” or “Too Low” 
#• If the number is guessed in ≤7 attempts, print success, else print the correct number. (CO2) 

import random

n = random.randint(1, 100)

for i in range(7):
    x = int(input("Guess the number: "))

    if x == n:
        print("Success")
        break
    elif x > n:
        print("Too High")
    else:
        print("Too Low")
else:
    print("Out of chances.\nThe correct number was:", n)
