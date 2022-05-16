print('******************************************   SELF   ***********************************')


class Student:
    standard = 8

    def printitems(self):
        return f" Name is {self.name},class is {self.standard} section is {self.section} & subjects are {self.subjects}"

    pass


captain = Student()
captain.name = 'Steve'
captain.section = "e"
captain.subjects = ['English', 'SST', 'Maths', 'Science']

shashank = Student()
shashank.name = 'Shashank'
shashank.section = "c"
shashank.subjects = ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit']

print(captain.printitems())
print(shashank.printitems())

print('******************************************   __INIT__   ***********************************')


class Student:
    standard = 8

    def __init__(self, name_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable

    pass


shashank = Student('Shashank', 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])
print(shashank.name)
print(shashank.section)
print(shashank.subjects)
