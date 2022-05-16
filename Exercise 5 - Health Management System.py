def getdate():
    import datetime
    return datetime.datetime.now()


def fn1(i):
    if i == 1:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Log ? "))
        if x == 1:
            y = str(input("Exercise = "))
            with open("Harry E.txt", 'a')as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")
        elif x == 2:
            y = str(input("Diet = "))
            with open("Harry D.txt", "a")as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")
    elif i == 2:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Log ? "))
        if x == 1:
            y = str(input("Exercise = "))
            with open("Rohan E.txt", "a")as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")
        elif x == 2:
            y = str(input("Diet = "))
            with open("Rohan D.txt", "a")as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")
    elif i == 3:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Log ? "))
        if x == 1:
            y = str(input("Exercise = "))
            with open("Hammad E.txt", "a")as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")
        elif x == 2:
            y = str(input("Diet = "))
            with open("Hammad D.txt", "a")as h:
                h.write(str([str(getdate())]) + " = " + y + "\n")
            print("Succesfully Written !")


def fn2(r):
    if r == 1:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Read ? "))
        if x == 1:
            with open("Harry E.txt") as w:
                print(w.readlines())
        elif x == 2:
            with open("Harry D.txt") as w:
                print(w.readlines())
    elif r == 2:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Read ? "))
        if x == 1:
            with open("Rohan E.txt") as w:
                print(w.readlines())
        elif x == 2:
            with open("Rohan D.txt") as w:
                print(w.readlines())
    elif r == 3:
        x = int(input("Choose 1 for Exercise , 2 for Diet\nWhat You Should Want To Read ? "))
        if x == 1:
            with open("Hammad E.txt") as w:
                print(w.readlines())
        elif x == 2:
            with open("Hammad D.txt") as w:
                print(w.readlines())


z = int(input("Choose 1 for Read, 2 for Retrive = "))
if z == 2:
    a = int(input("Choose 1 for Harry, 2 for Rohan, 3 for Hammad \nName = "))
    fn1(a)
elif z == 1:
    b = int(input("Choose 1 for Harry, 2 for Rohan, 3 for Hammad \nName = "))
    fn2(b)
