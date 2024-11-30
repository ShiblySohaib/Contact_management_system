import add_contact
import remove_contact
import view_contacts
import search_contact

#Note: Dummy contacts are given in contacts.txt

def app():
    try:
        #check if file already exists
        with open("contacts.txt", "r"):
            pass
    except:
        #if not, then create file
        with open("contacts.txt", "w"):
            pass


    while True:
        print("\t\tContact Management System")
        print("\t\t=========================\n")
        print("[1] Add contact")
        print("[2] Remove contact")
        print("[3] Search contact")
        print("[4] View all contacts")
        print("[0] Exit")

        choice = input("\nChoose an option: ")

        choice = int(choice) if choice.isnumeric() else None

        print("\n")

        if choice == 1:
            add_contact.add_contact()
        elif choice == 2:
            remove_contact.remove_contact()
        elif choice == 3:
            search_results = search_contact.search_contact()
            view_contacts.table_view(search_results)
        elif choice == 4:
            view_contacts.view_all_contacts()
        elif choice == 0:
            print("Thanks for using Contact Management System")
            exit()
        else:
            print("Invalid Choice. Try again")


        print("\n\n")


app()