def http_status(status):
    match status:
        case 200:
            return "Ok"
        
        case 404:
            return "Not found"
        
        case 500:
            return "Internal Server Error"
        
        case _:
            return "unkown status "


# print(http_status(4534))


# merging dictionary
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
merged = d1 | d2
# print(merged)