import random
number = random.randint(1, 1000)
tries = 1
user_guess = int(input("Guess a number between 1 and 1000: "))
while tries < 10:
    if user_guess == number:
        print("Correct!")
        print('You won :)))')
        break
    elif user_guess < number:
        print("Too low!")
        print(f"You have only {10 - tries} tries")
        user_guess = int(input("Guess a number between 1 and 1000: "))
        tries += 1
    else:
        print("Too high!")
        print(f"You have only {10 - tries} tries")
        user_guess = int(input("Guess a number between 1 and 1000: "))
        tries += 1
else:
    print("You lost! :(")
