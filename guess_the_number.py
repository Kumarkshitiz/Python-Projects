import random

top_range= input("Enter the Range ")
if top_range.isdigit():
    top_range = int(top_range)

    if top_range<=0:
        print("Please type a positive integer")
        quit()
else:
    print("Please type a number next time")
    quit()

random_num = random.randrange(0,top_range)
guess = 0

while True:
    guess += 1
    user_guess = int(input("Guess the number "))
    if user_guess == random_num :
        break
    elif user_guess <= random_num:
        print("Your guess is smaller than the Actual number")

    else:
        print("Your guess is larger than the Actual number")

print("Wow! , You Guessed it Right")

print("You took " + str( guess) + " Guesses")
