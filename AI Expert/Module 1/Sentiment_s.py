from textblob import TextBlob
print("Welcome to sentiment Spy!")
un = input("Please enter your name: ")
if not un:
    un = "Mysterious"
conversation_history = []
print (f"\n Hello, Agent {un}")
print("I am here to analyze the sentiment of your conversations.")
print(f"Type 'reset', 'history'  or 'exit' to quit the program.\n")
while True:
    ui = input(">>").strip()
    if not ui:
        print("Please enter a message.")
        continue
    if ui.lower() == "exit":
        print(f"Goodbye, Agent {un}!, come back again soon!")
        break
    
    if ui.lower() == "reset":
        conversation_history.clear()
        print("Conversation history has been reset.")
        continue
    if ui.lower() == "history":
        if not conversation_history:
            print("No conversation history yet.")
        else:
            print("Conversation History:")
            for idx, (text, polarity, sentiment) in enumerate(conversation_history, start=1):
                print(f"{idx}. {text} - Polarity: {polarity:.2f}, Sentiment: {sentiment}")
        continue
    polarity = TextBlob(ui).sentiment.polarity
    if polarity > 0.25:
        sentiment = "Positive"
    elif polarity < -0.25:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    conversation_history.append((ui, polarity, sentiment))
    print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})")

