class A:
    def printer(self):
        print("Method Of Class A.")


class B(A):
    def printer(self):
        print("Method Of Class B.")


class C(A):
    def printer(self):
        print("Method Of Class C.")


class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()

d.printer()
# "Method Of Class B." is printed because of the multiple inheritance.
# I you change the sequence of the multiple inhertance,i.e (B, C) to (C, B)  than the method 'ptinter()' will print "Method Of Class B."

# class A:
#     def printer(self):
#         print("Method Of Class A.")
#
#
# class B(A):
#     def printer(self):
#         print("Method Of Class B.")
#
#
# class C(A):
#     def printer(self):
#         print("Method Of Class C.")
#
#
# class D(C, B):
#     pass
#
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# d.printer()

