''' NAME- Daksh Joshi 
ENROLLMENT NUMBER- 01414002025  
SEM 3 SHIFT 1
5. Write a program that creates a CSV file storing product details (ID, Name, Price). Include a function to update the price of a given product ID. '''

import csv

def create_csv(fn):
    rows = [   ["ID", "Name", "Price"],
        [101, "Monitor", 12000],
        [102, "Mouse", 500],
        [103, "Keyboard", 1500]   ]

    with open(fn, "w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)
    print("CSV created.")

def update_price(fn, pid, new_p):
    rows = []
    found = False
    with open(fn, "r") as f:
        r = csv.reader(f)
        hdr = next(r)
        rows.append(hdr)
        for row in r:
            if int(row[0]) == pid:
                row[2] = new_p
                found = True
            rows.append(row)
    
    if found:
        with open(fn, "w", newline="") as f:
            w = csv.writer(f)
            w.writerows(rows)
        print(f"Price updated for ID {pid}.")
    else:
        print("Product ID not found.")

def show_csv(fn):
    with open(fn, "r") as f:
        for row in csv.reader(f):
            print(row)

fn = "products.csv"
create_csv(fn)
print("\nBefore update:")
show_csv(fn)

update_price(fn, 102, 750)

print("\nAfter update:")
show_csv(fn)

