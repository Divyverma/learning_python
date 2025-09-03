p1 = "Make a lot of money"
p2 = "buy now"
p3 = "sbscribe this"
p4 = "click this"


mess =  input("Enter text: ")
if((p1 in mess) or (p2 in mess) or (p3 in mess) or (p4 in mess)):
    print("It is a spam comment")
else:
    print("Not a spam comment")