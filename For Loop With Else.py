items = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
n = input("Enter A Number That Is Present On The List = ")
for item in items:
    if item == f'item {n}':
        break
else:
    print("Item Not Found !!")

# This 'else' statement will work if the loop was ended normally without any 'break' statement.
# In the following code if the 'if' statement was true the loop breaks and the next 'else' statement will not work.
# Otherwise it will work.
