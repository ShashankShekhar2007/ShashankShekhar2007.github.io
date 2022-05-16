# Comprehensions are used to write code in single line, it's used with lists, dictonaries and sets


# A list of numbers divisible by 3
list_1 = []
for i in range(100):
    if i % 3 == 0:
        list_1.append(i)
print(list_1)

list_2 = [i for i in range(100) if i % 3 == 0]
print(list_2)

# A Dictionary of numbers
dictionary_1 = {i: f"Item No.{i}" for i in range(1, 101)}
print(dictionary_1)

# To reverse key, values of a dictionary.
dictionary_2 = {i: f"Item No.{i}" for i in range(1, 11)}
dictionary_2 = {value: key for key, value in dictionary_2.items()}
print(dictionary_2)

# Sets
# Set comprehension only takes one value once.
set_1 = {i for i in [1, 1, 1, 1, 2, 2, 2, 423, 3, 5, 436, 5, 6, 7, 78, 67]}
print(type(set_1))
print(set_1)

# Generators of even numbers.
# NOTE:-  " () " brackets are used to create generators comprehension.
even_numbers = (i for i in range(101) if i % 2 == 0)
print(type(even_numbers))
for item in even_numbers:
    print(item)
