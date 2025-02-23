import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess the number (between 1 and 10)!")

while True:
    guess = int(input("Enter your guess: "))  # Get user input

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right!")
        break  # Exit the loop when the correct number is guessed
