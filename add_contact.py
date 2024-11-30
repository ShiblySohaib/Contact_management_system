import valid

def add_contact():
    name = input("Enter name: ").strip()
    #handle invalid names
    if not valid.name(name):
        print("\n\nInvalid name. Names can only contain letters and spaces.")
        return

    
    phone = input("Enter phone no: ").strip()
    #handle invalid phone numbers
    if not valid.phone(phone):
        print("\n\nInvalid phone number. Phone numbers can only contain digits and must be 7-15 digits in length.")
        return
    

    email = input("Enter email: ").strip()
    #handle invalid emails
    if not valid.email(email):
        print("\n\nInvalid email. Emails must be in this format: XXXXXX@XXX.XX (X can be a letter, digit or any special character except space, '@' and '.')")
        return
    

    address = input("Enter address: ").strip()


    #if it's not a duplicate, then add it
    with open("contacts.txt", "r+") as phonebook:
        for contact in phonebook:
            data = contact.split(',')
            if data[1].strip() == phone:
                print("\n\nContact already exists!")
                phonebook.close()
                return
        phonebook.write(f"\n{name},{phone},{email},{address}")
        print(f'\n\nContact "{name}" added succesfully!')




