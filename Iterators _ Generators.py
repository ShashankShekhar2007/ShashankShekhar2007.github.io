numbers = [5, 6, 4, 54, 67, 2, 34]
iterator = iter(numbers)
# The function 'iter()' simply converts the value in an object.
print(iterator)

# If you have to print the values of the object you have to use '__next__()'
# You can use it further to print the next value.
print(iterator.__next__())
print(iterator.__next__())
# **************  OR  **************************************************************
print(next(iterator))

# You can also use a loop to print all the values.

# for values in iterator:
#     print(values)

# As you can see that the values we had printed earlier aren't repeated...wow.

# You can also use it in function.

print('*******************************************************************************')


class TenTop:

    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.num
        if value <= 10:
            self.num += 1
            return self.num
        else:
            raise StopIteration


values = TenTop()
# print(values.__next__())
for i in values:
    print(i)

print('*****************************  GENERATOR  ***********************************************')


def gen(n):
    for i in range(n):
        yield i


generator = gen(25422780459)


# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())


# Factorial Generator

def factorial_generator(n):
    f = 1
    for value in range(n):
        f = f * (value + 1)
        yield f


# Recursion will not work here, because the function is considered as a generator once 'yield' is used.

x = factorial_generator(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


# ***************************************      OR        **********************************
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_generator2(x):
    i = 0
    while i <= x:
        yield factorial(i)
        i += 1


fac = factorial_generator2(10)
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())
print(fac.__next__())


# ************************************  FIBONACCI  ************************************


def fibonacci(n):
    if n == 1:
        yield 0
    elif n == 2:
        yield 1
    else:
        a, b = 0, 1
        for value in range(n):
            c = a + b
            a, b = b, c
            yield c


fib = fibonacci(10)
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
