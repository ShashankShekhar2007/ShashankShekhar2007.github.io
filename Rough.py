"""
x = input("Enter Your Name = ")
message = "would you like to learn some Python today ? "
print("Hello " + x + ", " + message)
"""
"""
name = input("Enter Your Name = ")
print(name.upper())
print(name.lower())
print(name.title())
"""
"""
fname = "Albert Einstein"
quote = 'once said, "A person who never made a mistake never tried anything new."'
print(fname + " " + quote)
"""
"""
var = 0.2 + 0.1
print(var)
var2 = 3 * 0.1
print(var2)
"""

# def afn(a, b):
#     av = (a + b) / 2
#     print(av)
#
#
# afn(4, 6)
#
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# print(getdate())


# favourite_number = {"shashank": "39", "captain": "2023", "iron man": "3000"}
#
# print(f"Shashank's favourite no. is {favourite_number['shashank']}")
# print(f"Captain's favourite no. is {favourite_number['captain']}")
# print(f"Iron Man's favourite no. is {favourite_number['iron man']}")
#
# print("\n*****************  OR  *****************\n")
#
# for key, value in favourite_number.items():
#     print(f"{key.title()}'s favourite no. is {value}")

# languages = {'a', 'e', 'd', 'e'}
# print(languages)

#
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# print(alien_0['color'])

# pizza = {
# 'crust': 'thick',
# 'toppings': ['mushrooms', 'extra cheese']
# }
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t", topping)

# favorite_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
#                       'phil': ['python', 'haskell'], }
#
# # for name, languages in favorite_languages.items():
# #     if len(languages) ==1:
# #         print(f"\n{name.title()}'s favorite language are:")
# #     elif len(languages) >= 2:
# #         print(f"\n{name.title()}'s favorite languages are:")
# #     for language in languages:
# #         print(f"\t{language.title()}")
# users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
#          'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', }, }
# print(users['aeinstein']['first'])

# d = {}
# x = str(input("Input your key = "))
# y = str(input("Input your value = "))
# # d.update({x: y})
# z = d[x] = y
# print(f'Updated Dictionary = {d}')


# x = int(input("How old are you ? "))
# abc = x > 18
# print(abc)
# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# *******************************   EXERCISE    *****************************************

# while True:
#     age = input('Enter Your Age OR Enter "quit" to exit: ')
#     if age == 'quit':
#         break
#     age = int(age)
#     if age <= 3:
#         print('Your Ticket Is Free')
#
#     elif age <= 12:
#         print('Your Ticket Is $10')
#
#     elif age > 12:
#         print('Your Ticket Is $15')

# import random
# lis = ['Hello!!', 'hi', 'bye']
# for value in range (5):
#     inp = input()
#     c = random.choice(lis)
#     print(f'{c}{inp} ')

# sandwich_orders = ['veggie', 'pastrami', 'pastrami', 'grilled cheese', 'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
# print("Sorry, We don't have pastrami anymore.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f'I am working on your {sandwich} sandwich.')
#     finished_sandwiches.append(sandwich)
# print('\n\n')
# while finished_sandwiches:
#     sandwich = finished_sandwiches.pop()
#
#     print(f'I made your {sandwich} sandwich.')

import time
from functools import lru_cache

# inp = int(input("How many values you want to cache = "))
#
#
# @lru_cache(maxsize=inp)
# def any_function(n):
#     time.sleep(n)
#     print("Executed.")
#
#
# any_function(3)
# any_function(4)
# any_function(5)
# print("Executing again...")
# any_function(3)
# any_function(4)
# any_function(5)
# print("Executed...")


import os

# def removeFiles(filen):
#     DNotDis = open(filen)
#     l = (DNotDis.read())
#     var = (l.split('\n'))
#     DNotDis.close()
#     return var
#
# def army(pathn, filen, ext):
#     filen=filen
#     pathn=pathn
#     os.chdir(pathn)
#     count = 0
#     var = removeFiles(filen)
#     for f in os.listdir():
#          f_name, f_ext = os.path.splitext(f)
#          if f_ext == f'.{ext}':
#              newName = f'{str(count)}{f_ext}'
#              count += 1
#              os.rename(f,newName)
#              pass
#          if f_name not in var:
#              tn = f_name.title()
#              new_name = f'{tn}{f_ext}'
#          else:
#              new_name = f'{f_name}{f_ext}'
#          os.rename(f,new_name)
#
# if __name__ == '__main__':
#     pathn = 'C://Folder'
#     filen ='Do Not Touch.txt'
#     ext = 'jpg'
#     army(pathn,filen,ext)

# def soldier(path,file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f :
#         filelist = f.read().split("\n")
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f'{i}{format}')
#             i +=1
# soldier(r"C:\Folder", r"C:\Folder\Do not touch.txt", '.jpg')
#
# i = int(input("Enter a Number = "))
# for x in range(i):
#     x+=1
#     print(x, end=",")


# def getdate():
#     import datetime
#     import time
#     return time.localtime()
#
# print(getdate())


# def renaming_function(path, format_f):
#     os.chdir(path)
#
#     for f in os.listdir():
#         file_n, file_f = os.path.splitext(f)
#         if file_f == f".{format_f}":
#             name = file_n.split('#')
#             new_name = f"{name[1]}.{name[0]}{file_f}"
#             os.rename(f, new_name)
#             pass
#         else:
#             n_name = f'{file_n}{file_f}'
#             os.rename(f, n_name)
#
#
# renaming_function(r'D:\Python\Tkinter\New folder', 'mp4')


# import numpy as np
# import cv2
#
# img = cv2.imread('Image.jpg')
# print(img.date)

('/storage/emulated/0/Download/Attendance/1.xlsx')
