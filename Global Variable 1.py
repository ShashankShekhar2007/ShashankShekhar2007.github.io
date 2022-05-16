x = 10  # Global Variable
y = 15  # Global Variable
def fn1():
    x = 5  # Local Variable
    y = 7  # Local Variable
    print(x, y)
fn1()

print(x, y)

def fn2():
    x = 5  # #Local Variable
    print(x, y)
fn2()

print(x, y)

# def fn3():
#     x = x + 10
#     y =7
#     print(x, y)
# fn3()

def fn4():
    global x
    x = x + 10
    y =7
    print(x, y)
fn4()

