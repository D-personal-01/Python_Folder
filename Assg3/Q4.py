''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
4. Write a Python program with two functions: one to create and write user details into a text file, and another to read and display the data. '''

def write_details(fn):
    nm = input("Enter name: ")
    ag = input("Enter age: ")
    cr = input("Enter course: ")
    with open(fn, "w") as f:
        f.write("Name: " + nm + "\n")
        f.write("Age: " + ag + "\n")
        f.write("Course: " + cr + "\n")
    print("Details saved.")

def read_details(fn):
    print("\n--- User Details ---")
    with open(fn, "r") as f:
        d = f.read()
    print(d)

fn = "user_info.txt"
write_details(fn)
read_details(fn)

