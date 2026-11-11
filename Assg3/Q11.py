''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
11. Write a Python script using NumPy to create a 1D array of 15 elements. Perform elementwise addition and multiplication with another array of same size. '''

import numpy as np

a1 = np.arange(1, 16)
a2 = np.arange(16, 31)

s = a1 + a2
p = a1 * a2

print("Array 1:\n", a1)
print("Array 2:\n", a2)
print("Addition:\n", s)
print("Multiplication:\n", p)
