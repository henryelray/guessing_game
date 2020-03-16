
# This is a number guessing game.
"""Program allows the computer to generate random numbers from 1 to 100
   The user's task is to guess the random number generated.The user  wins the game
   if his/her guess matches the randomly generated number in  10 or less attempts
   print a congratulation message else print a failed message and allow the the user to enter
    another number provided he/she hasn't exceeded the number of attempts
    Provide a way to display the previously entered number and how low or high the number entered is
"""

from random import randint


def generated_num():
    """Generates a random number between 1 and 100"""
    random_num = randint(1, 101)
    return random_num


def check_num():
    """Checks if number entered is equal to random number"""
    guess_count = 1

    while guess_count <= 10:

        rand_num = generated_num()
        guess_num = input("Guess a number\n")

        if guess_num == str(rand_num):
            print("Congratulations!!!")
            break
        else:
            print("Failed")

        guess_count += 1

        if guess_num > str(rand_num):
            print("Your guess is higher")

        elif guess_num < str(rand_num):
            print("Your guess is lower ")

        print("Random number is " + str(rand_num))
        print("Previously guessed number was "+guess_num+"\n")


check_num()


def game_status():
    """Asks the user if he wants to continue or not"""
    active = True
    while active:
        response = input("Do you want to play another game?(y/n)")
        if response == 'y':
            check_num()
        elif response == 'n':
            break


game_status()










