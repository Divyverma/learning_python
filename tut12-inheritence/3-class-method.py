# class Employee:
#     a = 1
#     @classmethod #this will show class attribute
#     def show(self):
#         print(f"The class value of a is {self.a}")
    

# e = Employee()
# e.a = 45

# e.show()




# property decorator

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self): 
        return self.ename
    
    @name.setter
    def name(self, value):
        self.ename = value



e = Employee()
e.a = 45

e.name = "divy"
print(e.name)

e.show()