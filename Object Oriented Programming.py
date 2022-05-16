class Student:
    standard = 8
    pass


captain = Student()
captain.name = 'Steve'
captain.section = "c"
captain.subjects = ['English', 'SST', 'Maths', 'Science']

shashank = Student()
shashank.name = 'Shashank'
shashank.section = "c"
shashank.subjects = ['Hindi', 'English', 'SST', 'Maths', 'Science', 'Sanskrit']

# You can access variable 'standard' by both instances 'shashank' or 'captain' .

print(shashank.standard)
print(captain.standard)
print(Student.standard)

# You can change the value of 'standard' PERMANENTLY by only using the class 'Student'.
print('\n*********************************************************************************************\n')
shashank.standard = 9  # It creates an instance variable of object 'shashank'.
print(shashank.standard)
print(Student.standard)
Student.standard = 9
print(Student.standard)

# To know the variables associated with object you can use '__dict__' attribute.

print('\n************************************************************************************************\n')

print(shashank.__dict__)  # You can see the instance variable 'standard' that we created earlier.

print(Student.__dict__)  # You can see the changed value of class variable 'standard'.
