class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = 0
    @property
    def marks(self):
        return self.markss
    @marks.setter
    def marks(self,value):
        if 0 <= value <= 100:
            self.markss = value
        else:
            raise ValueError("Marks must be between 0 and 100")
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
        print()
        


# example

stud1=student("A",19)
stud2=student("B",18)

stud1.marks=95
stud2.marks=98
# if i do stud2.marks=185 it will give an error because marks should be between 0 and 100

stud1.show()
stud2.show()