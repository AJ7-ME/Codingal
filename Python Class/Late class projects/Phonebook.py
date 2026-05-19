phonebook = {
    'travis': '555-1234',
    'xavier': '555-5678',
    'rakshan': '555-8765',
    'leo': '555-4321'
}
name1 = input("Enter a name: ")
name = name1.lower()
print("Number: ", phonebook.get(name, "Not found"))
delname= input("Enter a name to delete: ")
if delname in phonebook:
    del phonebook[delname]
    print(f"{delname} has been deleted from the phonebook.")
else:
    print(f"{delname} not found in the phonebook.")
print("Updated Phonebook:", phonebook)