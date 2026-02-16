import pickle
#Create record
def create():
    f=open("stud.dat","ab")

    roll=int(input("Enter roll number: "))
    CGP=int(input("Enter CGP: "))
    pickle.dump([roll,CGP],f)
    
    f.close()

    
#Display
def display():
    
    f=open("stud.dat","rb")
    
    try:
        while 1:
            s=pickle.load(f)
            print(f"\nRoll:{s[0]}\nCGP:{s[1]}\n")
    except EOFError:
        pass
    
    f.close()
#Search student record
def search():
    f=open("stud.dat","rb")

    try:
        while 1:
            s=pickle.load(f)
            if s[0]==roll:
                print(f"\nRoll:{s[0]}\nCGP:{s[1]}\n")
                f.close()
                return[s[0],s[1]]
    except EOFError:
        print("Student record not found ")
        f.close()

    
#Update CGP
def update():
    f=open("stud.dat","rb+")

    roll=int (input("Enter the roll number of the student: "))
    
    try:
        while 1:
            pos=pickle.tell()
            s=pickle.load(f)
            if s[0]==roll:
                print(f"\nRoll:{s[0]}\nCGP:{s[1]}\n")
                cgp=int(input("Enter the new CGP: "))
                seek()
                    
            
    
    f.close()

    
#Delete student record
def delete():
    f=open("stud.dat","ab")


    
    f.close()

    

print ("                                                                                   ------WELCOME TO STUDENT FILE------")

c=0

while c!=6:
        print ('''\n\nWhat opration do you want to perform:
                                                                                             1. Create a record.
                                                                                             2. Display record.
                                                                                             3. Search record.
                                                                                             4. Update record.
                                                                                             5. Delete record.
                                                                                              6. Exit.''')

        c=int(input("Enter the searies number to do do the opration: "))

        if c==1:
            create()
        elif c==2:
            display()
        elif c==3:
            search()
        elif c==4:
            update()
        elif c==5:
            delete()
        elif c==6:
            break
        else:
            print ("Incorrect choice please choose again.")















