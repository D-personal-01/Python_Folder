# Decorators modifies a function

def greet(fx):
    def dfx(*a, **b):
        print()
        print ("Good Morning")
        fx(*a,**b)
        print ()
        print ("Thanks for using this function")
        print ()
    return dfx

@greet
def addition(a,b):
    print ("Sum of both the terms are-\n",a+b)
    return

addition(2**14281,16**3571)
