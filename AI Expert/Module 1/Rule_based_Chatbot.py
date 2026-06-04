import re, random
destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui", "Bali"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes"],
    "cities": ["Paris", "New York", "Tokyo", "Rome"]
}
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
    "Why did the bicycle fall over? Because it was two-tired!"
    "Why did the tomato turn red? Because it saw the salad dressing!"
    "Why did the math book look sad? Because it had too many problems!"
    "Why did the coffee file a police report? It got mugged!"
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!"
    "Why did the chicken join a band? Because it had the drumsticks!"
    "Why did the computer go to the doctor? Because it had a virus!"
    "Why did the cookie go to the doctor? Because it was feeling crumbly!"
    "Why did the banana go to the doctor? Because it wasn't peeling well!"
    "Why did the skeleton go to the party alone? Because he had no body to go with him!"
]
tips = ["- Pack light and versatile clothing."
    "- Don't forget your travel documents and chargers."
    "- Bring a reusable water bottle and snacks."
    "- Consider the weather and activities you'll be doing."
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print("TravelBot: Beaches, Mountains or cities?")
    preference = input("You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"TravelBot: I recommend visiting {suggestion}!")
        print("TravelBot: Do you like the recommendation? (yes/no)")
        feedback = input("You: ").strip().lower()
        if feedback == "yes":
            print("TravelBot: Great! I hope you have an amazing trip!")
        else:
            print("TravelBot: No worries! Let's try again.")
            recommend()
    else:
        print("TravelBot: Sorry, I didn't understand that. Please choose from beaches, mountains, or cities.")
    show_help()
def packing_tips():
    print("TravelBot: Where to?")
    location = normalize_input(input("You: "))
    print("TravelBot: How many days?")
    days = input("You: ")
    print(f"TravelBot: Here are some packing tips for your {days}-day trip to {location}:{random.choice(tips)}         ")
def tell_joke():
    print(f"TravelBot: Here's a travel joke for you: {random.choice(jokes)}")
def show_help():
    print("\nTravelBot: I can help you with the following:")
    print("- Type 'recommend' for travel destination suggestions.")
    print("- Type 'packing' for packing tips.")
    print("- Type 'joke' for a travel-related joke.")
    print("- Type 'exit' or 'bye' to quit the chatbot.\n")
def chat():
    print("Welcome to TravelBot! How can I assist you today?")
    print("Type 'help' to see what I can do.")
    name =input("Whats your name?\n")
    print(f"TravelBot: Hello, {name}! Let's chat about travel!")
    show_help()
    while True:
        user_input = input(f"{name}: ")
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "packing" in user_input or "pack" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif user_input in ["exit", "bye"]:
            print(f"TravelBot: Goodbye, {name}! Safe travels!")
            break
        else:
            print("TravelBot: I'm sorry, I didn't understand that. Type 'help' to see what I can do.")
if __name__ == "__main__":
    chat()