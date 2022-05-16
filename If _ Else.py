"""x = 50
y = 100
z = int(input("Your Number = "))
if y<z:
    print("More Than 100")
elif y==z:
    print("Equal to 100")
else:
    print("Less Than 100")

if x<z:
    print("More Than 50")
elif x==z:
    print("Equal to 50")
else:
    print("Less Than 50")


l = [12, 34, 56, 778, 89, 2, 3, 4, 5, 6]
print(12 in l)
if 12 in l:
    print("Yes")
"""
#quiz
print("What is your age ?")
age = int(input())

if 90 < age:
    print('You cannot drive because you are over-aged !')
elif 18 < age:
        print("You can drive 👍!")
elif 18 > age:
    print('You cannot drive because your age is not enough !')
elif 18 == age:
    print("Cannot Tell")