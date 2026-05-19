while True:

    print("Right angled pattern of ^")
    n =  int(input("Enter the number of rows:\n"))
    x = str(input("What character do you want to make up the triangle, Just saying 1 character looks best: "))
    for i in range(n):
        for j in range(i+1):
            print(x, end="")
        print()