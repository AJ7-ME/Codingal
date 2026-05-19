import random

def number_guessing_game():
    """A simple number guessing game"""
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        guessed = False
        
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("Can you guess it?\n")
        print("🎯 Hint: Try to guess the number in as few attempts as possible!\n")
        print("(Type 'end' to restart the game)\n")
        
        while not guessed:
            try:
                guess = input("Enter your guess: ")
                
                if guess.lower() == "end":
                    print("\nRestarting the game...\n")
                    break
                
                guess = int(guess)
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                attempts += 1
                
                if guess < secret_number:
                    print("Think higher.\n")
                elif guess > secret_number:
                    print("Think lower.\n")
                else:
                    print(f"\n🎉 Correct! You guessed it in {attempts} attempts!")
                    guessed = True
            
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    number_guessing_game()