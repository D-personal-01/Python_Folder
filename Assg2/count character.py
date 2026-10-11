#Q6. Create a tuple from user input, and write a function to count how many times each element appears using dictionary operations. 

def charcount(t1):
    d={}
    for i in t1:
        d[i]=t1.count(i)
    return d

t1=eval(input("Enter the tuple in tuple form '()' :"))
print(charcount(t1))