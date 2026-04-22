# Write your code here
import random
# Set secret number
secret_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 99")
# Ask the user to guess

while True:
    guess = input("Enter a guess: ")
    if not guess.isdecimal():
        print("That's NOT a number")
        continue

    guess = int(guess)
    if guess == secret_number:
        print("You are a genius! That's correct!")
        break
    elif guess < secret_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

# Check to see if the guess is <, >, or = secret number
# Print the right message