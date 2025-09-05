# ques1

# import random
# def game():
#     score =  random.randint(1, 20)

#     with open("score.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"you score: {score}")
#     if(score>hiscore):
#         with open("score.txt", "w") as f:
#             f.write(str(score))
    
#     return score

# game()





# ques2
# def replace():
#     with open("file.txt", "r") as f:
#         data = f.read()
        
#     data = data.replace("donkey", "####")
    
#     with open("file.txt", "w") as f:
#         f.write(data)


# replace()





# ques3
# def repMore():
#     words = ["donkey", "bad", "ganda"]
    
#     with open("file.txt", "r") as f:
#         content = f.read()

#     for item in words:
#         content  = content.replace(item, "####")
    
#     with open("file.txt", "w") as f:
#         f.write(content)

# repMore()





# ques4
# def find():
#     with  open("file.txt", "r") as f:
#         data = f.read()

#     if("python" in data):
#         print("Yes")
#     else:
#         print("No")

# find()





# ques5

# def findLine():
    
#     with open("file.txt", "r") as f:
#         lines = f.readlines()
    
#     lineNo = 1
#     for line in lines:
#         if("python" in line):
#             print(f"yes, line no. {lineNo}")
#             break
#         lineNo+=1
#     else:
#         print("not present")
# findLine()





# ques5
# def copy():
#     with open("file.txt", "r") as f:
#         data = f.read()
#     with open("copy_file.txt", "w") as new:
#         new.write(data)

# copy()





# ques6
# def checkSame():
#     with open("file.txt") as f:
#         content1 = f.read()

#     with open("myfile.txt") as f:
#         content2 = f.read()


#     if(content1 == content2):
#         print("same")
#     else:
#         print("Not Same")

# checkSame()