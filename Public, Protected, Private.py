class Student:
    standard = 8
    _protec = 12
    __private = 47

    def __init__(self, name_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable

    def subject_printer(self):
        for subject in self.subjects:
            print(subject)

    @staticmethod
    def message_printer(message):
        print(f"Your message is {message}")


shashank = Student('Shashank', 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])


class Children(Student):
    def __init__(self, name_variable, section_variable, subjects_variable, school_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable
        self.school = school_variable


babu_bhaiya = Children('Babu Rao Ganpat Rao Apte', 'XYZ', ['Marathi', 'Gujarati'], 'Oxford Vidyalaya Of Ramgarh')


# TO use protected variable you can use simple "_" .
print(f'Protected Variable = {babu_bhaiya._protec}')

# TO use private variable you can use "_" with the name of class "Student" (in which the private variable is made) .
print(f'Private Variable = {shashank._Student__private}')
