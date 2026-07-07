# Decorators are used to modify a function.

def greet(fx):
    def dfx(*a, **b):
        print()
        print ("Good Morning")
        fx(*a,**b)
        print ()
        print ("Thanks for using this function")
        print ()
    return dfx
# We can use it like this
def addition(a,b):
    print ("Sum of both the terms are-\n",a+b)
    return

greet(addition(2,5))
greet(addition(234,348))

# But instad of repeating again and again we can use this.

@greet
def addition(a,b):
    print ("Sum of both the terms are-\n",a+b)
    return

addition(2**14281,16**3571)

