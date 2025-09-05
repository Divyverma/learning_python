class Employee:
    language = "py" #class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}")

    @staticmethod #now this will not take/need self
    def greet():
        print("Good Morning")


Divy = Employee()
Divy.name = "Divy" #object attribute
Divy.language = "javascript" #instance attribute

# print(Divy.name, Divy.language, Divy.salary)

Divy.getInfo()
Employee.getInfo(Divy)