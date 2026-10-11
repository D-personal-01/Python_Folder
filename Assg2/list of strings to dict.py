def strtodict(s1):
    print(s1)
    d={}
    for i in s1:
        d[i]=len(i)
    return d

s1=(input('Enter the words seprated by space :'))
s1=s1.split()
print(strtodict(s1))
