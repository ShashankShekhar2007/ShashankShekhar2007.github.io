import os

print(dir(os))

print(os.getcwd())
# This function "getcwd" means get current working directory , which tells you that in which directory you are working
# You can change this directory in the case required.

os.chdir('C://')
print(os.getcwd())
# Now you can see that the directory has been changed.


print(os.listdir())
# This will show you what are the content available in the following directory.
# To know about the content of a specific directory you've to simply enter the directory in  "listdir()"
print(os.listdir('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject'))
print(os.listdir('C:/Users/Shashank Shekhar/Documents/Books'))

os.chdir('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject')
# This is to get back in our physical or real directory.


# os.mkdir("New Folder")
# This function is used to create a directory or folder.

# os.makedirs("New Folder/Sub Folder")
# This will create a sub directory inside "New Folder".
# If you'll change the name of the main directory "New Folder" to something else,
# it will create a new directory and then a sub directory in it.


# os.rename("Rec.py", "Rec.py")
# This will rename the following file


print(os.environ.get("Path"))
# This will help you to get environment variable.


print(os.path.join("C/", "Shashank Shekhar.txt"))
# This will help you to join the paths and without any error of slash(/ or \).


print(os.path.exists('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject'))
# This function will tell you whether a directory exists or not.


print(os.path.isdir('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject'))
# This function will tell you whether the following is a directory or not.


print(os.path.isfile('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject'))
print(os.path.isfile('C:/Users/Shashank Shekhar/PycharmProjects/pythonProject/Read.txt'))
# This function will tell you whether the following is a file or not.

