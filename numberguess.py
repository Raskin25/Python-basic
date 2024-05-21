import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    while True:
        user_input = input("Guess a number between 1 and 10: ")
        if user_input.isdigit():
            guess = int(user_input)
            if guess == number_to_guess:
                print("Congratulations! You found the number.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
        else:
            print("Please enter a number!")

guess_the_number()