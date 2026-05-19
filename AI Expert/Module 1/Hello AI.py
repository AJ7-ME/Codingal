print("Hello! I am an AI bot, What is your name?")
name = input("Enter your name: ")
print(f"Nice to meet you, {name}! I am here to assist you with any questions you may have about AI. Feel free to ask me anything!")
print("How are you feeling today? (Good/Bad)")
mood  = input().lower()
if mood == "good":
    print("That's great to hear! I'm glad you're feeling good.")
elif mood == "bad":  
    print("I'm sorry to hear that. If there's anything I can do to help, please let me know.")
else: print("I didn't understand that. Please enter 'Good' or 'Bad'.")
print(f"it was nice talking to you, {name}! If you have any more questions about AI, don't hesitate to ask. Have a great day!")