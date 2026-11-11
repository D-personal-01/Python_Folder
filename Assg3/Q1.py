''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
1. Write a Python function that accepts a list of numbers and returns a new list containing only the even numbers. Use both default and keyword arguments in your function call. '''

def get_evens(nums, lim=None):
    res = []
    for x in nums:
        if x % 2 == 0:
            res.append(x)
            if lim is not None and len(res) == lim:
                break
    return res

l = [12, 7, 18, 21, 24, 30, 35, 42]
print("Default arg call:", get_evens(l))
print("Keyword arg call:", get_evens(nums=l, lim=3))
