# n! = n * n-1 * n-2 * n-3 ....
# n! = (n-1)!
# Iterative Function
n = int(input("Enter A Number = "))
# def factorial_i(x):
#     f = 1
#     for i in range(x):
#         f = f * (i+1)
#     return f
# print(factorial_i(n))
#
# # Recursive Function
#
# def factorial_r(x):
#     if x == 1:
#         return 1
#     else :
#         return x * factorial_r(x-1)
# print(factorial_r(n))
# 0,1,1,2,3,5,8,13,21,34
def fibonacci(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(n))




































