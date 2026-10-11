#Q3. Write a Python function that accepts a list of strings and returns a dictionary with each string as the key and its length as the value. 

def strtodict(s1):
    print(s1)
    d={}
    for i in s1:
        d[i]=len(i)
    return d

s1=(input('Enter the words seprated by space :'))
s1=s1.split()
print(strtodict(s1))
