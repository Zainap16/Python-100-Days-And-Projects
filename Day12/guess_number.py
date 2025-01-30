import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

random_number = random.randrange(0,100,5)

# user_guess = int(input("Guess a number: "))

def check_guess():
    if user_guess > random_number:
        print("too high")
    elif user_guess < random_number:
        print("too low")

if level_mode.lower() == "easy" or level_mode.lower() == "e":
    attempts = 10
    while attempts <= 10 and attempts  > 0:
        user_guess = int(input("Guess a number: "))
        if user_guess == random_number:
            print("you win")
            break
        print(f"attempts: {attempts}\nrandom number: {random_number}")
        check_guess()
        attempts -= 1
elif level_mode.lower() == "hard" or level_mode.lower() == "h":
    attempts = 5
    while attempts <= 5 and attempts > 0:
        user_guess = int(input("Guess a number: "))
        if user_guess == random_number:
            print("you win")
            break
        print(f"attempts: {attempts}\nrandom number: {random_number}")
        check_guess()
        attempts -= 1







