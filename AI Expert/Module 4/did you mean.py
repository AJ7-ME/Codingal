MENU = {
    "pizza": 10,
    "burger": 8,
    "salad": 6,
    "soda": 2,
    "nachos": 5,
    "pasta": 12,
    "ice cream": 4,
    "fries": 3,
    "chicken wings": 9,
    "steak": 15,
    "soup": 7,
    "sandwich": 6,
    "tacos": 8,
}
def show_menu():
    print("\n" + "=" * 40)
    print("                  FOOD MENU")
    print("=" * 40)

    print(f"{'No.':<5}{'Item':<20}{'Price ($)':>10}")
    print("-" * 40)
    for number, (food, price) in enumerate(MENU.items(), start=1):
        print(f"{number:<5}{food:<20}{price:>10}")

    print("=" * 40)
def edit_distance(word1, word2):
    table = []
    for i in range(len(word1) + 1):
        row = []
        for j in range(len(word2) + 1):
                row.append(0)
        table.append(row)

    for i in range(len(word1) + 1):
        table[i][0] = i
    for j in range(len(word2) + 1):
        table[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
               cost = 0
            else:
                cost = 1
            delete = table[i - 1][j] + 1
            insert = table[i][j - 1] + 1
            substitute = table[i - 1][j - 1] + cost
            table[i][j] = min(delete, insert, substitute)
    return table[len(word1)][len(word2)]
def suggest_food(query):
    ranked = []
    for food in MENU:
        distance = edit_distance(query, food)
        ranked.append((distance, food))
        ranked.sort()
        return ranked[:3]

def search_food(query):
    query = query.lower().strip()
    if query in MENU:
        print("\n Correct spelling!")
        print("Food name :", query.title())
        print("Price ($) :", MENU[query])
        return 
    suggestions = suggest_food(query)
    if not suggestions:
        print("\nNo suggestions found.")
        return
    best_distance, best_food = suggestions[0]
    print("\nDid you mean:", best_food.title())
    print("Other suggestions:")
    for number, (distance, food) in enumerate(suggestions[1:], start=1):
        print(f"{number}. {food.title():<15}"
              f"Distance: {distance}"
              f"Price ($): {MENU[food]}")

print("Welcome to the Food Menu Search!")
show_menu()
while True:
    query = input("\nEnter a food name to search (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        print("Thank you for using the Food Menu Search. Goodbye!")
        break
    if query.strip() == "":
        print("Please enter a valid food name.")
        continue
    search_food(query)