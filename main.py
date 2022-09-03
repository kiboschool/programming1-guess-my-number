import random

# Set secret number
secret_number = random.randint(1,99)

print("I'm thinking of a number between 1 and 99")

# Ask the user to guess
# Check to see if the guess is <, >, or = secret number
# Print the right message
while True:  
  guess = input("Enter a guess: ")
  if not guess.isdecimal():
    print("that's not a number")
  elif int(guess) > secret_number:
    print("Your guess is too high")
  elif int(guess) < secret_number:
    print("Your guess is too low")
  else:
    print("Congrats! The number was", secret_number)
    break