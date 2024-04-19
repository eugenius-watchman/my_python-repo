# Generate random number
import random


secret = random.randint(1, 50)

# Set guess to zero
guess = 0

# Set trials to zero
trials = 0

# Set while loop
while guess != secret and trials < 5:

    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Your guess is too low")
    elif guess > secret:
        print("Your guess is too high.")

    trials += 1

# if guess == secret --> you won
if guess == secret:
    print("You won! It took you ", trials, " trials to guess that number. ")
else:
    print("Oops...You lost ! Better luck next time.")
