# Guess The Number
import random
print("***********************************************************")
var_a = int(input('Enter the value of "a" = '))
var_b = int(input('Enter the value of "b" = '))
print("***********************************************************")
numbers = []
for i in range(var_a,var_b):
    numbers.append(i)

number = random.choice(numbers)
print("\n***********************************************************")
print('Player 1:')
v = int(input(f'\nGuess a number between {var_a} & {var_b} = '))
x = True
count_1 = 1
while x is True:
    if v == number:
        print("\n***********************************************************")
        print(f'Player 1 Guessed the number in "{count_1}" chance(s).')
        print("***********************************************************")
        x = False
    else:
        count_1+=1
        v = int(input(f'Guess a number again = '))

print("\n\n***********************************************************")
print('Player 2:')
v2 = int(input(f'\nGuess a number between {var_a} & {var_b} = '))
x = True
count_2 = 1
while x is True:
    if v2 == number:
        print("\n***********************************************************")
        print(f'Player 2 Guessed the number in "{count_2}" chance(s).')
        print("***********************************************************")
        x = False
    else:
        count_2+=1
        v2 = int(input(f'Guess a number again = '))

print("\n\n***********************************************************")
print("********************** FINAL RESULT ***********************")
if count_1 < count_2:   
    print(" Player 1 is the Winner!!!") 
elif count_1 > count_2:
    print(" Player 2 is the Winner!!!")
elif count_1 == count_2:
    print("Match is Drawn!!!")
print("***********************************************************")