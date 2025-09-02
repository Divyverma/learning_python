name = input("enter the name")

print("Good Afternoon", name)
date = 23.2
print(f"Dear Divyansh\n {name} \nYou are selected! \n{date}")

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", name).replace("|Date|", "Sep 2050"))