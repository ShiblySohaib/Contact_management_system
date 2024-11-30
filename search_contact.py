import valid
import view_contacts

def search_contact():
    print("\t\tSearch Contact")
    print("\t\t==============\n")
    print("[1] Search by name")
    print("[2] Search by phone")
    print("[3] Search by email")
    print("[4] Search by address")
    print('\n[Note: You can do partial search (Example: "shi" will show both "shibly" and "shihab")]')

    choice = input("\nChoose an option: ")

    choice = int(choice) if choice.isnumeric() else None

    print("\n")

    if choice == 1:
        query = input("Enter name: ").strip()
    elif choice == 2:
        query = input("Enter email: ").strip()
    elif choice == 3:
        query = input("Enter phone no: ").strip()
    elif choice == 4:
        query = input("Enter address: ").strip()        
    else:
        print("Invalid Choice.")
        return



    search_results = []

    with open("contacts.txt", "r") as phonebook:
        for contact in phonebook:
            data = contact.split(',')
            if query.lower() in data[choice-1].strip().lower():
                search_results.append(contact)
    
    return search_results



            



