""" Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
Ask the user for their guess.
If they guess correctly, print 'You win!' and break.
Decrement guesses_left by one.
Use an else: case after your while loop to print You lose."""
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
count = 0


while guesses_left > 0: 
    guess = int(input("Your guess: "))
    guesses_left = guesses_left - 1
    if guess == random_number:
        print ("You win!")
        break
else:
    print ("You lose")