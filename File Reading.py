"""
x = open("Read.txt")
text = x.read()
print(text)
x.close()

            # OR

x = open("", "rt")
text = x.read()
print(text)


x = open("Read.txt", "rb")
text = x.read()
print(text)


x = open("Read.txt", "rt")
text = x.read(6)
print(text)
text = x.read(2)
print(text)

x.close()
"""



"""
x = open("Read.txt", "rt")
text = x.read()
for line in text:
    print(line)


x = open("Read.txt", "rt")
for line in x:                                      # do not type "text" type "x"
    print(line, end="")
    
x.close()

"""



x = open("Read.txt")
print(x.readline())
print(x.readline())


x = open("Read.txt")
print(x.readlines())


x.close()