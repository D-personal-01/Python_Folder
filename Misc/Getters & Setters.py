#class value:
 #   def __init__(self,value):
  #      self.value=value
  #   
  #  def show(self):
  #      print(self.value)

#obj=value(10)
#obj.show() # acts as a method and prints the value of the variable

class value:
    def __init__(self,value):
        self.value=value
    @property # acts as a getter method
    def expo_20(self):
        return self.value**20
    @ expo_20.setter # acts as a setter method
    def expo_20(self,value):
        self.value=value**(1/20)
    def show(self):
        print(self.value)
        print(self.expo_20)
    

obj=value(10)
obj.show()
print(obj.expo_20) # acts as an attribute and prints the value of the variable

