inp=input("Enter a number or write quit to exit: ")
if inp.lower()=="quit":
    print(f"you wrote {inp} exiting the program")
    quit()

inp=int(inp)
try:
    if inp <= 0 or inp > 1000:
       raise ValueError("Number must be between 1 and 1000")
except ValueError:
    raise 
    
print(f"You entered the number {inp}")
for i in range(1,inp+1):
    print("Lets make this world a better place!")

