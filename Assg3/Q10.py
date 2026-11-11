''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
10. Write a Python script to read a list of names from a text file, insert a new name at a given position, and save the modified list back to the file. '''

def insert_name(fn, nm, pos):
    with open(fn, "r") as f:
        names = f.readlines()
    
    names.insert(pos - 1, nm + "\n")
    
    with open(fn, "w") as f:
        f.writelines(names)
    print(f"'{nm}' inserted at position {pos}.")

fn = "names.txt"
with open(fn, "w") as f:
    f.write("Aman\n")
    f.write("Rishi\n")
    f.write("Priyal\n")

print("Original file:")
with open(fn, "r") as f:
    print(f.read())

insert_name(fn, "Daksh", 2)

print("Updated file:")
with open(fn, "r") as f:
    print(f.read())
