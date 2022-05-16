n1 = input("Enter A Number = ")
n2 = input("Enter Another Number = ")
try:
    print("Sum = ",
          int(n1)+int(n2))
except Exception as x :
    print(x)

print("Important Line")