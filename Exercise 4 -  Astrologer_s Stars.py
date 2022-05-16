try:
    i = int(input("No. Of Rows You Want = "))
    b = int(input("Choose Boolean Value (1 or 0) = "))
    if i>0 and b == 1:
        for x in range(i):
            print((x+1) * '*')
            i = i - 1
    elif i>0 and b == 0:
        for x in range(i):
            print(i * '*')
            i = i - 1
except Exception as x:
    print("Invalid Input")