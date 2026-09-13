class A():
    def __init__(self):
        print("Constructor of class A")
        super().__init__()  # Call the constructor of the next class in MRO

class B(A):
    def __init__(self):
        print("Constructor of class B")
        super().__init__()  # Call the constructor of the next class in MRO

class C(A):
    def __init__(self):
        print("Constructor of class C")
        super().__init__()  # Call the constructor of the next class in MRO

class D(B,C):
    def __init__(self):
        print("Constructor of class D")
        super().__init__()  # Call the constructor of the next class in MRO

class G(A,D):
    def __init__(self):
        print("Constructor of class G")
        super().__init__()  # Call the constructor of the next class in MRO

