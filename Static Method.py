class Student:
    standard = 8

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
print(shashank.name)

Student.message_printer("Hello !!")
shashank.message_printer("Hi !!")

print('\n\n***********************************************************************\n\n', shashank.subjects)
shashank.subject_printer()
