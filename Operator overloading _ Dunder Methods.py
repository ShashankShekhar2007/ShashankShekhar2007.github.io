class Student:
    standard = 8

    def __init__(self, name_variable, roll_no_variable, section_variable, subjects_variable):
        self.name = name_variable
        self.roll = roll_no_variable
        self.section = section_variable
        self.subjects = subjects_variable

    def __add__(self, other):  # "other" is the name of the other instance "babu_bahiya".
        return self.roll + other.roll

    def __truediv__(self, other):
        return self.roll / other.roll

    def __repr__(self):
        return f"Student's name is {self.name}, roll number is {self.roll}, {self.name} studies {self.subjects}."

    def __str__(self):
        return f"Student's name is {self.name}."


shashank = Student('Shashank', 39, 'C', ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit'])
babu_bhaiya = Student('Babu Rao Ganpat Rao Apte', 420, 'XYZ', ['Marathi', 'Gujarati'])
print(babu_bhaiya / shashank)
print(shashank + babu_bhaiya)
"""
NOTE:-
If you use the operator "+" between any two classes, then python will automatically define these 
classes to the function "__add__" and add the following instance variables (if they are integers) or 
do anything according to the operator defined (return self.roll * other.roll) for example if you use "*" instead of "+" 
it will be multiplied , but remind when you define it you have to only use "+" like this "print(shashank + babu_bhaiya)"
"""

print(shashank)
print(repr(babu_bhaiya))

"""
NOTE:-
What you write in "__repr__" or "__str__" will be returned when you will print the Instance.
Remember, when both "__repr__" and "__str__" are present in your class then python give first priority to "__str__"
So, if you have to use the "__repr__" in this condition you should use it like this "" print(repr(object)) ""
you can also use the same thing with "__str__" like "" print(str(object)) ""
"""
