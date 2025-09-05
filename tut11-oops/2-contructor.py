class Employee:
    language = "py" #class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # this is dunder method which is automatically called w/ calling
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}")

    @staticmethod #now this will not take/need self
    def greet():
        print("Good Morning")


Divy = Employee("divy", 13000, "javascript")
# Divy.name = "Divy"
print(Divy.name, Divy.salary, Divy.language)