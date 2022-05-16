# y = open("Write.txt", "w")
# y.write("Shashank ")
# y.close()


# y = open("Write.txt", "a")
# y.write("Shashank\n")
# y.close()


# y = open("Write.txt", "a")
# x = y.write("Shashank\n")
# print(x)
# y.close()


y = open("Write.txt", "r+")
print(y.read())
y.write("Shashank\n")
y.close()
