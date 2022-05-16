class A:
    classvar1 = "Class Variable Of 'Class A'."

    def __init__(self):
        self.var1 = "Instance Variable Of Instance 'a'."
        self.classvar1 = "2nd Instance Variable Of Instance 'a'."


class B(A):
    classvar1 = "Class Variable Of 'Class b'."


a = A()
b = B()

print(b.classvar1)
# Python first try to find the variable in Instance of "b" ,and then in Instance of "a.
# After that Python try to find the variable in Class "B" and then in Class "A".


class C:
    classvar2 = "Class Variable Of 'Class C'."

    def __init__(self):
        self.var1 = "Instance Variable Of Instance 'c'."
        self.classvar1 = "2nd Instance Variable Of Instance 'c'."
        self.special_var = "Special Variable Of Instance 'c'."


class D(C):
    classvar2 = "Class Variable Of 'Class D'."

    def __init__(self):
        super().__init__()
        self.var1 = "Instance Variable Of Instance 'd'."
        self.classvar1 = "2nd Instance Variable Of Instance 'd'."


c = C()
d = D()
print(d.var1)
print(d.special_var)
# Using super() Python will combine all Instance Variables of Instances "c" & "d".
# And override the variables with same name.
# Just like copy and paste system of Windows where the files with same name are overrided and other are copied.
