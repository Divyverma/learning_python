# prime number
# n = int(input("enter num: "))

# for i in range(2, n):
#     if(n%i) == 0:
#         print("num is not prime")
#         break
# else:
#     print("num is prime")



# factorial of a number
n = int(input("enter num: "))
product = 1
for i in range(1, n+1):
    product = product*i

print(product)