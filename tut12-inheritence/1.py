class Employee:
    company = "firstComp"
    def show(self):
        print(f"The name is {self.name} ans the salary is {self.salary}")

# making a new class from parent class and taking its all method in child class
class Programmer(Employee):
    company = "secComp"
    def showLang(self):
        print(f"The name is {self.name} ans he is good with {self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)