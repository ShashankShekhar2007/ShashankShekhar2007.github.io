class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.mail = f'{self.fname}.{self.lname}@gamil.com'

    def info(self):
        return f'My name is {self.fname} {self.lname}.'


shashank = Student('Shashank', 'Shekhar')
shashank.fname = 'Captain'
print(shashank.mail)


# The 'fname' of the instance 'shashank' was not changing.
# Lets solve it by  using a function of mail not a variable.

class Student2:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        return f'My name is {self.fname} {self.lname}.'

    def mail(self):
        return f'{self.fname}.{self.lname}@gmail.com'


babu_rao = Student2('Babu', 'Apte')
print(babu_rao.mail())
babu_rao.fname = 'Babu Rao'
print(babu_rao.mail())

# Lets make it more Pythonic , without calling the function 'mail' by making it aan attribute.
# You have to use the decorator "@property"

class Student3:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        return f'My name is {self.fname} {self.lname}.'
    @property
    def mail(self):
        return f'{self.fname}.{self.lname}@gmail.com'




babu_rao2 = Student('Babu', 'Apte')
print(babu_rao2.mail)
babu_rao2.fname = 'Babu Rao'
print(babu_rao2.mail)







class Student4:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        return f'My name is {self.fname} {self.lname}.'
    @property
    def mail(self):
        if self.fname == None or self.lname == None :
            return 'Set the mail'

        return f'{self.fname}.{self.lname}@gmail.com'
    @mail.setter
    def mail(self, string):
        name = string.split('@')[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]
        """
        This function split the given mail and according to the mail it will set or change the 
        instance variable 'fname' and 'lname' . And then the mail funtion made earlier work on 
        it and make it a mail.
        %%%% REMEBBER that the 'faname' and 'lname' was changed
        """


    @mail.deleter
    def mail(self):
        self.fname = None
        self.lname = None
        """
        We cannot delete it we have to make it 'None' and set use a 'if' statement 
        in the function 'mail' used under @property.
        """
captain = Student4('Steve', 'Rogers')
captain.mail = 'steve.peggy@gmail.com'
# We cannot change the attribute directly, we need to make a 'setter' for this.

print(captain.mail)
# Now it's changed.




# What if you have to delete this new mail, you cannot do it directlylike this:
# del captain.mail  , We have to make a 'deleter' for it.

del captain.mail
print(captain.mail)

# Now you can set the mail again if wanted.

captain.mail = 'steve.bucky@mail.com'
print(captain.mail)

