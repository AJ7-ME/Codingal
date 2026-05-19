print("what type of food sounds good at this very moment? ")
print("1. some thing sugary sweet") #Weird candy
print("2. some thing crispy") # potato chips
print("3. some thing salty") # Fries
print("4. some thing spicy") # Momos
print("5. some thing sour") # lemonade
print("6. some thing bitter") # dark chocolate
print("7. some thing healthy") # salad
answer = input("Enter the number of your choice: \n")
if answer == "1":
    print("You chose something sugary sweet! I would suggest having some hard sugar coated candies. Enjoy :)")
elif answer == "2":    print("You chose something crispy! I would suggest having some potato chips. Enjoy :)")
elif answer == "3":    print("You chose something salty! I would suggest having some fries or maybe some popcorn. Enjoy your movie :)")
elif answer == "4":    print("You chose something spicy! I would suggest having some momos (indian dumplings). Enjoy :)")
elif answer == "5":    print("You chose something sour! I would suggest having some lemonade. Enjoy :)")
elif answer == "6":    print("You chose something bitter! I would suggest having some dark chocolate. Enjoy :)")
elif answer == "7":    print("You chose something healthy! I would suggest having some salad or just protein powder. Enjoy :)")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")
    