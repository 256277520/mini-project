import random

top_of_range = input("type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0,top_of_range)




while True:
    user_guess = input("Guess a number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("Congrats you've won $8000 ")
        break
    else:
        print("You lost better luck next time")
