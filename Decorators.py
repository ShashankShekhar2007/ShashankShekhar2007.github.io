def f1():
    print("Hello World!")


f2 = f1
del f1
f2()


def executor(name_of_function):
    name_of_function("This")


executor(print)


# ***************************************     DECORATOR    ************************************

def decorator1(function):
    def new_function():
        print("\nExecuting")
        function()
        print("Executed")

    return new_function



@decorator1
def func():
    print("Hello !!!!!!!!")


func()
