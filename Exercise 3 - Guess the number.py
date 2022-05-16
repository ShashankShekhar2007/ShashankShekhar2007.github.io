print("Let's Start The Game !! \nGuess The Number ?")
your_options = ("(a).12\n(b).14\n(c).19\n(d).18\n(e).34\n(f).23")
print(your_options)
guesses = 1
while guesses <= 3:
    i = int(input("Your Number = "))
    if i==18:
        print("Congratulations !! You Win The Game.")
    elif i>= 19:
        print("Choose Smaller One.")
    elif i<=17:
        print("Choose Greater One.")
    else:
        print("No.Of Guesses You Take = ", guesses)
        break
    print(3 - guesses, "Guesses left")
    guesses = guesses + 1
if guesses > 3:
    print("Game Over")




