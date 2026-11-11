''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
3. Define a function that accepts a variable number of arguments and returns their sum. Demonstrate the difference between formal and actual arguments. '''

def calc_sum(*vals):
    s = 0
    for v in vals:
        s += v
    return s

a, b, c, d = 5, 10, 15, 20
tot = calc_sum(a, b, c, d)

print("Formal argument: *vals inside calc_sum")
print(f"Actual arguments: {a}, {b}, {c}, {d}")
print("Sum =", tot)
