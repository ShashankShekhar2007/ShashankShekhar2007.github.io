"""
x = 0
while (True ):
    print(x+1, end =" ")
    x = x + 1
"""
"""
x = 0
while (True ):
    print(x+1, end =" ")
    if x==44:
        break
    x = x + 1
"""
"""
x = 0
while (True ):
    if x+1<10:
        x=x+1
        continue
    print(x+1, end =" ")
    if x==44:
        x=x+1
        break
    x = x + 1
"""
# quiz

while (True):
    i = int(input("Your Number = "))
    if i > 100:
        print("Congratulations !! Your Number Is Greater Than 100 ")
        break
    else:
        print("Try Again !!")
        continue
