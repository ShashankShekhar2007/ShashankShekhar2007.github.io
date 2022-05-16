# --------------------------------------MAP-------------------------------------------
num = ['1', '2', '4']
num = list(map(int, num))
op = num[1] + 2
print(op)
num = list(map(lambda x: x * x, num))
print(num)



num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def square(x):
    return x * x
def cube(x):
    return x * x * x
func = [square, cube]
print("\n-----------------Squares & Cubes-------------- ")
for item in num2:
    a = list(map(lambda x: x(item), func))
    print(f"\n{a}")


# --------------------------------------FILTER-------------------------------------------

l1 = [1,2,3,4,5,6,7,8,9,10]
def greater_than_5(n):
    return n > 5

#Return the value in TRUE or FALSE


b = list(filter(greater_than_5, l1))
print("\n\n\n", b)


# --------------------------------------REDUCE-------------------------------------------
from functools import reduce
l2 = [1,2,3,4,5]
c = reduce(lambda x,y:x+y, l2)
print("\n\n\n",c)