import os
# specify the directory (here we use current directory ".")
directory = "/home/divyansh/Documents"

# list all files and folders in the directory
contents = os.listdir(directory)

print("Contents of directory:", directory)
for item in contents:
    print(item)
