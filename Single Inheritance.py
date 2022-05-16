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


class Children(Student):
#Using Inheritance you can use all functions, instanace variables & class variables indirectly it's a copy of class "Student"
    def __init__(self, name_variable, section_variable, subjects_variable, school_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable
        self.school = school_variable


babu_bhaiya = Children('Babu Rao Ganpat Rao Apte', 'XYZ', ['Marathi', 'Gujarati'], 'Oxford Vidyalaya Of Ramgarh')
print(f"{babu_bhaiya.name}'s school name is {babu_bhaiya.school}.")
print(babu_bhaiya.subject_printer())


