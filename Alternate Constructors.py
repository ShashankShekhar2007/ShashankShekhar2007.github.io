class Student:
    standard = 8

    def __init__(self, name_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable

    @classmethod
    def from_shlash(cls, string):
        list = string.split('/')
        return cls(list[0], list[1], list[2])
    # ***************************   OR    **********************************************************
    @classmethod
    def from_shlash2(cls, string):
        return cls(*string.split('/'))


# "cls" is denoted to the class associated with the instance or object to which function is used

shashank = Student('Shashank', 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])
print(shashank.name)
captain = Student.from_shlash('Captain/D/English')
print(captain.standard)


captain = Student.from_shlash2('Captain/D/English')
print(captain.standard)