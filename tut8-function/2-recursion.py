def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

print(fact(5))

def sumN(n):
    if(n==0):
        return 0
    return n+sumN(n-1)

print(sumN(10))


''''
for n = 3
***
**
*
'''

def pattern(n):
    for i in range(0, n):
        print("*"*(n-i), end="")
        print(" "*i)

pattern(3)


# remove a word from a list and strip it at the same time
list = ["Harry", "Rohan", "Shubham", "an"]

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    

print(rem(list, "an"))
