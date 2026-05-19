import random
secret_number = str(random.randint(1, 100))
print("Welcome to the Guessing Game!")
print("I will generate a random number between 1 and 100.")
print("Guess the number!")
count = 1
try:
    while True:
        num = int(input("Enter your guess: "))
        if num < 1 or num > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if str(num) == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            print(f"You took {count} attempts to guess {secret_number}.")
            break
        elif str(num) > secret_number:
            print("Try again! Your guess is too high.")
            count = count + 1
        elif str(num) < secret_number:
            print("Try again! Your guess is too low.")
            count = count + 1
except ValueError:
    print("Invalid input! Please enter a valid number between 1 and 100.")
    
