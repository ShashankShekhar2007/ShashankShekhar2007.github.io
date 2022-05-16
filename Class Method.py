class Student:
    standard = 8

    def __init__(self, name_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable

    @classmethod
    def standard_change(cls, new_standard):
        cls.standard = new_standard

# "cls" is denoted to the class associated with the instance or object to which function is used

shashank = Student('Shashank', 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])
print(shashank.name)

shashank.standard_change(9)
print(shashank.standard)
