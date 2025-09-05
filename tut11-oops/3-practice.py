# ques1
# class programmer:
#     company = "microsoft"

#     def __init__(self, name, salary, language):
#         self.name = name
#         self.salary = salary
#         self.language = language


# p1 = programmer("prog1", 120000, "js")
# print(p1.name, p1.salary, p1.language)


# ques2
# class calci:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"square of Num: {self.n*self.n},")

#     def cube(self):
#         print(f"cube of Num: {self.n*self.n*self.n},")

#     def sqaureRoot(self):
#         print(f"square root of Num: {self.n ** 0.5}")

# a = calci(4)
# a.square()
# a.cube()
# a.sqaureRoot()




# ques3

# class demo:
#     a = 4

# o = demo()
# print(o.a)
# o.a = 0
# print(o.a)
# print(demo.a)





# ques4
# import random

# class train:

#     def __init__(self, trainNo):
#         self.trainNo = trainNo
#     def book(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(1000, 5000)}")

# t = train(12300)
# t.book("Delhi", "Noida")
# t.getStatus()
# t.getFare("Delhi", "Noida")




