l = ["a", "b", "c", "d"]

i = 0
for value in l:
    if i % 2 != 0:
        print(f"Variable {value}")
    i += 1

print("\n\nEnumerate Function:-\n")
for index, value in enumerate(l):
    if index % 2 != 0:
        print(f"Variable {value}")
