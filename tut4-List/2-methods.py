friends = ["apple", "orange", 3, 3.44, False, "rohan"]

friends.append("Harry")  #end me harry ghuss jayega list
# print(friends)


l1 = [1, 3, 2, 44, 22, 23, 534]
l1.sort() #sort the list in increasing order
print(l1)
l1.reverse() #reverse the list 
print(l1)


# inserting an item at wanted index
l1.insert(3, 444) # 444 inserted at index 3
print(l1)


val = l1.pop(3) #pop the indexed value and return it
print(val)
print(l1)

# removes a value
l1.remove(22) # 22 is a value not an index
print(l1)