while True:
    print("Say 1 for Addition")
    print("Say 2 for Subtraction")
    print("Say 3 for Multiplication")
    print("Say 4 for Division")
    print("Say 5 for Exponentiation (first number to the power of second number)\n")

    process = input("what process do you want to do?\n")
    if process not in ["1","2","3","4","5"]:
        print("\ninvalid input\n")
        continue

    x = float(input("what is your first number?\n"))
    y = float(input("what is your second number?\n"))

    if process == "1":
        print("your answer is:",x + y,"\n")
    elif process =="2":
        print("your answer is: ",x - y,"\n")
    elif process =="3":
        print("your answer is: ",x * y,"\n")
    elif process =="4":
        print("your answer is: ",x / y,"\n")
    elif process == "5":
        print("your answer is: ",x ** y,"\n")
    else:
        print("invalid input\n")