
class value:
    def __init__(self,value):
        self.value=value
    @property # acts as a getter method
    def show(self):
        print(self.value)

obj=value(10)
obj.show # acts as a attribute and prints the value of the variable
    
