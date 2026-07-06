# Class--> blueprint
#  Objects--> Entities

# Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Objects are instances of classes, representing specific entities with their own unique data and behavior.
# Objects are created from classes and can have their own state (attributes) and behavior (methods). Each object can have different values for its attributes, allowing for the creation of multiple instances of the same class with varying characteristics.

# Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, known as a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
# Inheritance is a mechanism in object-oriented programming (OOP) that allows a class (called a subclass or derived class) to inherit properties and behaviors (attributes and methods) from another class (called a superclass or base class). This promotes code reusability and establishes a hierarchical relationship between classes, enabling the creation of specialized classes based on existing ones.
# Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). Polymorphism can be achieved through method overriding (where a subclass provides a specific implementation of a method defined in its superclass) and method overloading (where multiple methods have the same name but differ in parameters). This allows for flexibility and extensibility in code, as the same operation can behave differently based on the object it is acting upon.

# Employee representation using a class

class Emp:
    name = "John Doe"
    occupation = "Software Engineer"

print(f"Employee Name: {Emp.name}\nOccupation: {Emp.occupation}")



