''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
7. Create a Python module named `mathutils.py` containing functions for square, cube, and factorial. Import this module and call its functions in another program. '''

def square(n):
    return n * n

def cube(n):
    return n * n * n

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

