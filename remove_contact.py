import valid

def remove_contact():
    found = False
    print("[Note: Entering name will remove every contact with that name]\n")
    query = input("Enter name or phone number: ").strip()
    if valid.name(query):
        qtype = 0
    elif valid.phone(query):
        qtype = 1
    else:
        print("\n\nInvalid search query!")
        print("# Phone numbers can only contain digits and must be 7-15 digits in length.")
        print("# Names can only contain letters and spaces.")
        return
    

    with open("contacts.txt", "r") as phonebook:
        contacts = phonebook.readlines()

    with open("contacts.txt", "w") as phonebook:
        for contact in contacts:
            data = contact.split(',')
            if data[qtype].strip().lower() == query.lower():
                found = True
                name = data[0].strip()
                continue
            phonebook.write(contact)
    
    if found:
        print(f'\n\nContact "{name}" removed successfully!')
    else:
        print("\n\nContact not found.")
                





