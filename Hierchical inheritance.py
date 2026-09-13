class base():
    def __init__(self):
        self.str1 = "Hello"
        print("\nBase class constructor called.\n")

    def display(self):
        print(self.str1)

class derived1(base):
    def __init__(self):
        base.__init__(self)
        print("Derived1 class constructor called.\n")

class derived2(base):
    def __init__(self):
        base.__init__(self)
        print("Derived2 class constructor called.\n")

#As we have writen the derived 1 first and then derived 2, the constructor of derived 1 will be called first and then derived 2.
class derived3(derived1, derived2):
    def __init__(self):
        derived1.__init__(self)
        derived2.__init__(self)
        print("Derived3 class constructor called.\n")

a= derived3()