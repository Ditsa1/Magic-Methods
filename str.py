class Employee:   

    def __init__(self):
        self.name="Python"
        self.sal = "0"

    def __str__(self):
        return "Name:" + self.name + " Salary:" + str(self.sal)

emp = Employee()
print(emp)