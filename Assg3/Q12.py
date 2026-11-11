''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
12. Create a 3x5 NumPy array with random integers. Reshape it into a 5x3 array and calculate the sum of all elements row-wise and column-wise. '''

import numpy as np

arr = np.random.randint(1, 10, size=(3, 5))
print("Original 3x5 Array:\n", arr)

arr_5x3 = arr.reshape(5, 3)
print("\nReshaped 5x3 Array:\n", arr_5x3)

r_sum = np.sum(arr_5x3, axis=1)
c_sum = np.sum(arr_5x3, axis=0)

print("\nRow-wise Sum:\n", r_sum)
print("Column-wise Sum:\n", c_sum)
