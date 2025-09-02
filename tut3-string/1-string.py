a = 'string'
b = "string"
c = '''string''' # all of the above are string


# indexing in string
'''
        0    1   2   3   4
        d    i   v   y   a
        -5  -4  -3  -2  -1
'''


# slicing in string
name = "divyansh"
nameShort = name[0:4] #this will slice the string from 0th index to 4th
print(nameShort)

char1 = name[1]
print(char1)

print("0th to 4th: ", name[:4]) #starting from 0th index to 4th index
print("2nth to len-1: ", name[2:]) #starting from 2nd index to (len-1) index


# skipping in string --> you can skip the charactors in the string

s = "newstring"
new = s[1:6:2]  # first it take 1 to 6 char from the string and removes the 2nd char from it
print(new)
