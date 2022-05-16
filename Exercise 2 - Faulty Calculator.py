#Exercise 2 - Faulty Calculator
#45*3 , 56+9, 56/6

try:
    inp1 = int(input("First Number = "))
    inp3 = (input("Operation = "))
    inp2 = int(input("Second Number = "))
    if inp1 == int(45) and inp2 == int(3) and inp3 == ("*"):
        print("555")
    elif inp1 == int(3) and inp2 == int(45) and inp3 == ("*"):
        print("555")
    elif inp1 == int(56) and inp2 == int(9) and inp3 == ("+"):
        print("77")
    elif inp1 == int(9) and inp2 == int(56) and inp3 == ("+"):
        print("77")
    elif inp1 == int(56) and inp2 == int(6) and inp3 == ("/"):
        print("4")
    elif inp3 == "*":
        print(int(inp1) * int(inp2))
    elif inp3 == "+":
        print(int(inp1) + int(inp2))
    elif inp3 == "-":
        print(int(inp1) - int(inp2))
    elif inp3 == "/":
        print(int(inp1) / int(inp2))
    else:
        print("Error ! Please Check Your Input.")

except:
    print("Wrong Input")