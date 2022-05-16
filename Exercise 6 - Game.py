# Game - Rock , Paper ,Scissor
# R ="Rock"
# P = "Paper"
# S = "Scissor"
import random
import time
h = 0
co = 0
choices = 10
chance = 0
print("Use Capital Letters !!!")
while chance < choices:
    lst = ['R', 'P', 'S']
    c = random.choice(lst)
    i = str(input("Choose: 'R' For Rock , 'P' For Paper , 'S' For Scissor = "))
    if c == "R" and i == "P":
        h = h + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Win")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "P" and i == "S":
        h = h + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Win")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "S" and i == "R":
        h = h + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Win")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "R" and i == "S":
        co = co + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Lose")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "P" and i == "R":
        co = co + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Lose")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "S" and i == "P":
        co = co + 1
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("You Lose")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "R" and i == "R":
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("Tie")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "P" and i == "P":
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("Tie")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    elif c == "S" and i == "S":
        print(f"Your choice is '{i}' , Computer choice is '{c}'")
        print("Tie")
        chance = chance + 1
        r = 10 - chance
        print(f"Now you have {r} chances\n")
    else:
        print("Wrong Input")

print(f"\nTotal Score:\nYour Score = {h} \nComputer Score = {co}")
if h > co:
    print("You Won The Match !!!")
elif co > h:
    print("You Lose The Match !!!")
elif co == h:
    print("Match is Drawn")

time.sleep(10)

