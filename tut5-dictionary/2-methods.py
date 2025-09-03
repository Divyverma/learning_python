marks = {
    "divy":100,
    "shubh":43,
    "rohan":32
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"divy":88, "ren":44})
# print(marks)

print(marks.get("divy")) #if the key does not present in the dict then it gets none
