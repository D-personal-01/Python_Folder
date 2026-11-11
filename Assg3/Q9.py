''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
9. Write a function that reads a binary file and counts how many times a given byte value occurs in the file. '''

def count_byte(fn, val):
    with open(fn, "rb") as f:
        data = f.read()
    return data.count(bytes([val]))

fn = "sample.bin"
with open(fn, "wb") as f:
    f.write(bytes([10, 20, 10, 30, 10, 40, 20]))

b_val = 10
cnt = count_byte(fn, b_val)
print(f"Byte {b_val} occurs {cnt} times in {fn}.")
