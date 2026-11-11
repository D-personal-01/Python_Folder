''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
2. Create a recursive Python function to calculate the nth number in the Fibonacci sequence. Call the function with user input. '''

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci number is: {fib(n)}")

