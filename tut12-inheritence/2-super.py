class employee:
    def __init__(self):
        print("constructor of employee")
    a=1


class Programmer(employee):
    def __init__(self):
        print("constructor of Programmer")
    b=1


class Manager(Programmer):
    def __init__(self):
        super().__init__() #this will also runs its parent class constructor
        print("constructor of Manager")
    c=1


Man = Manager()
print(Man.a, Man.b, Man.c)