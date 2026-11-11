''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
6. Demonstrate the concept of local and global scope with a Python function that modifies a global variable inside a nested function. '''

x = 50

def outer():
    y = 25
    
    def inner():
        global x
        x = 100
        print("Inside inner(): x =", x)
        
    inner()
    print("Inside outer(): y =", y)

print("Before outer(): x =", x)
outer()
print("After outer(): x =", x)
