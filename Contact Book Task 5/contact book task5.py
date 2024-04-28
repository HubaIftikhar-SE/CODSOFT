# List to store names and contacts
names = []
phone_numbers = []

# Display name and contact
def names_contacts():
    print("\tName\t\t\tPhone Number")
    for i in range(len(names)):
        print(f'\t{names[i]}\t\t\t{phone_numbers[i]}')

# Searching from inputs 
def search_contact(name):
    if name in names:
        index = names.index(name)
        print(f"Contact found:\n\tName: {names[index]}\n\tPhone Number: {phone_numbers[index]}")
    else:
        print("Contact not found.")

# Storing contacts and names
num = 3
for i in range(num):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    names.append(name)
    phone_numbers.append(phone_number)

# Calling the function
names_contacts()

# Search for a contact
search_name = input("Enter the Name to search: ")
search_contact(search_name)
