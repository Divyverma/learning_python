# try:
#     a = int(input("Enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)




# zero division error
# a = int(input("Enter a number: "))
# b = int(input("Enter sec number: "))


# if(b==0):
#     raise ZeroDivisionError("can't divide by zero")
# else:
#     print(f"The division a/b is {a/b}")



# try ans else
# try:
#     a = int(input("Enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)
# else:
#     print("hi") #if exception wasn't run then else block executed



# try and finally
try:
    a = int(input("Enter num: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("Inside finally")