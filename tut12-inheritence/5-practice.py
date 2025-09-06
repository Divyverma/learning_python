# ques 1
# class twoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")


# class threeDVector(twoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# a = twoDVector(4, 2)
# a.show()
# b = threeDVector(4, 2, 3)
# b.show()





# ques 2
# class Animal:
#     pass


# class Pets(Animal):
#     pass


# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("bow bow")

# d = Dog()
# d.bark()


# ques 3
# class Employee:
#     salary = 234
#     increament = 20

#     @property
#     def salaryAfterIncreament(self):
#         return (self.salary + self.salary * (self.increament/100))


# e = Employee()
# print(e.salaryAfterIncreament)




# ques 4
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1+c2)