# print(list1[0],list1[1], list1[2])
# list1 = [["Shashank", "shashank"] , ["Shekhar","shekhar"] ,["Singh","singh"] ,["Captain","captain"] ,["Steve", "steve"], ["Rogers","rogers"]]
"""
list1 = [["Shashank", 1], ["Shekhar", 2], ["Singh", 3], ["Captain", 4], ["Steve", 5], ["Roger", 6]]
for item, numbers in list1:
    print(item, numbers)
for item, numbers in list1:
    print(item, "is number", numbers)


d1 = dict(list1)
print(d1)
for item, numbers in d1.items():
    print(item, "is number", numbers)

for things in d1:
    print(things)
"""
list1 = ["Shashank", "Shekhar", 2, "Singh", 32, "Captain", 4, "Steve", 55, "Roger", 11, 6]
for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)

# While Loop
x = 0
while x < 100:
    print(x)
    x = x + 1
