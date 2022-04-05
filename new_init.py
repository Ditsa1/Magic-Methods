class Employee:
    def __new__(cls):
        print("New magic method called.")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("Init magic method called.")

emp = Employee()