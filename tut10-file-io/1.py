''''
a = "very long string with emails"

'''

# how to read a file

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()


# how to write a file

# st="hey this is amazing"
# f = open("myfile.txt", "w")  #here w means you want to write in the file
# f.write(st)
# f.close()



# more function/methods

# f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()


# append mode

# f = open("file.txt", "a")
# dat = "\ni am adding this"
# f.write(dat)
# f.close()


# with statement

# f = open("file.txt")
# print(f.read())
# f.close()

# the above whole thing can be written using with statement 
# and u don't have to close the file

with open("file.txt") as f:
    print(f.read())