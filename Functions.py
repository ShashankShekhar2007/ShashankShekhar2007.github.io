a = 3
b = 10
c = sum((a, b))  # built in function
print(c)


def fn1():
    print("Hello World")


fn1()
print(fn1())


def fn2(a, b):
    print("Hello World", a * b)


fn2(2, 3)


def afn(a, b):
    av = (a + b) / 2
    print(av)


afn(4, 6)


def bfn(a, b):
    av = (a + b) / 2
    # print(av)
    return av


x = bfn(4, 6)
print(x)


def cfn(a, b):
    """Formula of Average"""
    av = (a + b) / 2
    return av


print(cfn.__doc__)
