# Class--> blueprint
#  Objects--> Entities

# Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Objects are instances of classes, representing specific entities with their own unique data and behavior.
# Objects are created from classes and can have their own state (attributes) and behavior (methods). Each object can have different values for its attributes, allowing for the creation of multiple instances of the same class with varying characteristics.

# Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, known as a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
# Inheritance is a mechanism in object-oriented programming (OOP) that allows a class (called a subclass or derived class) to inherit properties and behaviors (attributes and methods) from another class (called a superclass or base class). This promotes code reusability and establishes a hierarchical relationship between classes, enabling the creation of specialized classes based on existing ones.
# Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). Polymorphism can be achieved through method overriding (where a subclass provides a specific implementation of a method defined in its superclass) and method overloading (where multiple methods have the same name but differ in parameters). This allows for flexibility and extensibility in code, as the same operation can behave differently based on the object it is acting upon.

# Employee representation using a class

class Emp:

    # Static variable to keep track of the employee number
    company_name = "ABC_Co-op"
    occupation=""

    # Constructor method to initialize the attributes of the Employee class
    def __init__(self, name, position, occupation, salary, IQ, EQ, total_projects, num_success_projects):

        self.name = name
        self.position = position
        self.occupation = occupation
        self.salary = salary
        self.IQ= IQ
        self.EQ= EQ
        self.total_projects = total_projects
        self.num_success_projects = num_success_projects
        self.proj_success_rate = 100*(num_success_projects / total_projects if total_projects > 0 else 0)
        self.employee_rating= ((self.IQ + self.EQ) / 2 + self.proj_success_rate)/10


    def display_info(self):

        print(f"Company: {Emp.company_name}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Occupation: {self.occupation}")
        print(f"Salary: ${self.salary}")
        print(f"Employee Rating: {self.employee_rating}")

# Creating objects (instances) of the Employee class
a=Emp("A","Accountant","CA",50000,120,80,10,7)
b=Emp("B","Manager","BCA",60000,130,90,15,12)
c=Emp("C","Developer","B.tech",55000,125,85,8,6)

# Updating the attributes of the objects
a.salary=55000
b.position="Senior Manager"

# Displaying the information of each employee using the display_info method
a.display_info()
b.display_info()
c.display_info()


