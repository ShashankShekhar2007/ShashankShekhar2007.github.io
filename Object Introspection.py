class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        return f'My name is {self.fname} {self.lname}.'

    @property
    def mail(self):
        if self.fname == None or self.lname == None:
            return 'Set the mail'

        return f'{self.fname}.{self.lname}@gmail.com'

    @mail.setter
    def mail(self, string):
        name = string.split('@')[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]

    @mail.deleter
    def mail(self):
        self.fname = None
        self.lname = None


shashank = Student('Shashank', 'Shekhar')

print(shashank.mail)
# ****************************    TYPE    **************************************
print(type('this is a string.'))
# 'type' function shows the class to which the following object belong.


# ****************************    ID    **************************************


print(id(shashank))
# The 'id' function shows the ID af any object , in python every object have an ID .
# Same object have same ID, remember if any object have any minor change the ID will be different.
print(id('shashank'))
print(id('Shashank'))

# ****************************    DIR    **************************************

# 'dir' function shows all the modules defined under a following object.
print(dir('shashank shekhar'))

# When you use it with any class object it will show the modules and functions in it.
# In the object 'shashank' you can see the functions (info and mail) at the last of the list printed.
print(dir(shashank))


# ****************************    INSPECT   **************************************
import inspect

#The inspect module helps in checking the objects present in the code that we have written.

print(inspect.getmembers(shashank))