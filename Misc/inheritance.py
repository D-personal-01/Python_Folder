class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_info(self):
        print(f"Name: {self.name}, ID: {self.id}")
        print()

class C_level_emp(employee):
    def __init__(self,shares):
        self.shares=shares
    def show_info(self):
        super().show_info()
        print(f"Shares: {self.shares}")
        print()

# example
emp1=employee("Alice",1)
emp2=employee("Bob",2)

emp1.show_info()
emp2.show_info()