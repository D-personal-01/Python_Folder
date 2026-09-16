
#Q5. Create a simple login simulation where: 
#• A user is given 3 attempts to enter the correct password 
#• The stored password is 'Python@123' 
#• If the password is correct within 3 tries, print "Login Successful" • Else print "Account Locked" 

i=0
x="Python@123"
while (i<3):
  p=input("Enter the password: ")
  if x==p:
    print("successful login ")
    break
  else:
    print("wrong password pls try again  ")
    i+=1

if i == 3:
    print("Account Locked")