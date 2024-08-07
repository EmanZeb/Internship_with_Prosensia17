 import random
    targetNumber = random.randint(1, 100)
    attempts = 0
    maxAttempts = 10

    while attempts < maxAttempts:
        guess = int(input("Guess the number: "))
        attempts += 1
        if guess == targetNumber:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < targetNumber:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {target_number}.")

guessNumber()
