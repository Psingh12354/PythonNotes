class Employee:
    def __new__(cls):
        print("__new__magic method is executed.")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ magic method is executed.")
        self.name="Priyanshu"
        self.salary=10000
    def __str__(self):
        return "Name="+self.name+" Salary="+str(self.salary) #implicitily call
e1=Employee()
print(e1.name)
print(e1) #implicit calling
