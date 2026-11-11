''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
8. Write a Python function to delete a specific line from a text file given a line number. Ensure the file is rewritten without that line. '''

def delete_line(fn, ln):
    with open(fn, "r") as f:
        lines = f.readlines()
    
    if 1 <= ln <= len(lines):
        del lines[ln - 1]
        with open(fn, "w") as f:
            f.writelines(lines)
        print(f"Line {ln} deleted successfully.")
    else:
        print("Invalid line number.")

fn = "data.txt"
with open(fn, "w") as f:
    f.write("Line 1: Python Programming\n")
    f.write("Line 2: Data Structures\n")
    f.write("Line 3: File Handling\n")

print("File before deletion:")
with open(fn, "r") as f:
    print(f.read())

delete_line(fn, 2)

print("File after deletion:")
with open(fn, "r") as f:
    print(f.read())
