a=input("Enter the the messege to encode it: ")
list(a)
encoded=""
for i in a:
    s=(ord(i))**3+25*66/100
    encoded=encoded+str(s)
    print(encoded)
