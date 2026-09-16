#Q4. Take an integer n and print the following pattern using nested loops: (CO1)
#*
#* *
#* * *
#* * * *
#till n lines


n=int(input("Enter the number: "))
for i in range(1, n):
    for j in range(i):
        print("* ", end="")
    print()