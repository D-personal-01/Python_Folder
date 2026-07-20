#Python doesn't have access modifiers like public, private, protected. But we can use name mangling to make a variable private. We can use double underscore before the variable name to indicate it private but in real it is not private.
#(__) is used to make a variable private but it is not really private. It is just a way to avoid accidental access of the variable. We can access the private variable using name mangling which makes private variable more like a variable not to be accidently used.
class employee:
    def __init__(self):
        self.__name="Daksh"

a=employee()
print(a.__dir__()) #We can find name of the private variable using __dir__() method and access it using name mangling which makes private variable more like a variable not to be accidently used.
print(a._employee__name) #Accessing private variable using name mangling.
#print(a.__name) #This will give an error because we are trying to access private variable directly.

#(_) indicates a protected variable. It can be accessed by the class and its subclasses but not by other classes.
class employees:
    def __init__(self):
        self._name="Daksh" 

a=employees()
print(dir(employees)) #We can find name of the protected variable using __dir__() method and access it using name mangling which makes protected variable more like a variable not to be accidently used.
print(a._name) #Accessing protected variable directly. It is not recommended to access protected variable directly but it is possible.