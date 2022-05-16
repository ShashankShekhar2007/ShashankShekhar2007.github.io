class Student:
    standard = 8

    def __init__(self, name_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.section = section_variable
        self.subjects = subjects_variable


    @staticmethod
    def message_printer(message):
        print(f"Your message is {message}")


shashank = Student('Shashank', 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])
print(shashank.name)


class Player:
    def __init__(self, player_name, game):
        self.player_name = player_name
        self.game = game

    def game_printer(self):
        print(self.game)


    def subject_printer(self):
        for subject in self.subjects:
            print(subject)


class Children(Student, Player): #Python try to find the method anf functions in the first class mentioned i.e, "Student"
    pass


babu_bhaiya = Children('Babu Rao Ganpat Rao Apte', 'XYZ', ['Marathi', 'Gujarati'])
babu_bhaiya.subject_printer()