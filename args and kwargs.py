lst = ['name', 'name2', 'name3']
lst2 = [1, 2, 3, 4]
lst3 = {'1':'11', '2':'22', '3':'33', '4':'44'}


# def f(a, b, c):
#     for value in a:
#         print(value)
# f(list)

def f2(a, *args, **kwargs):
    for value in a:
        print(value)
    for val in args:
        print(val)
    for x, z in kwargs.items():
        print(z)
    print('\n**************\n')
# Args & Kwargs are optional if you don't add any argument the function will run normally.
# You can name anything in place of args and kwargs
# But don't remove the stars


f2(lst)
f2(lst, *lst2)
f2(lst2, *lst, **lst3)
