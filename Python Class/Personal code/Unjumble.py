from itertools import permutations
letters  = input("Enter the letters to unjumble: ")
perms = permutations(letters)
count = 0
print(len(perms))
for p in perms:
    print("".join(p))
    count += 1