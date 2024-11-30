#show argument contacts as table
def table_view(contacts):
    if not contacts:
        print("No contact found!")
        return
    nameWidth = 8
    phoneWidth = 9
    emailWidth = 9
    addressWidth = 11

    #get max width for each data
    for contact in contacts:
        data = contact.split(',')
        nameWidth = max(nameWidth, len(data[0].strip())+4) #4 is for minimum 2 spaces on both sides + 2 '|'
        phoneWidth = max(phoneWidth, len(data[1].strip())+4)
        emailWidth = max(emailWidth, len(data[2].strip())+4)
        addressWidth = max(addressWidth, len(data[3].strip())+4)


    width = nameWidth + phoneWidth + emailWidth + addressWidth - 3

    #insert categories as the first row
    contacts.insert(0, "Name, Phone, Email, Address\n")

    for contact in contacts:
        data = list(contact.split(','))
        print(width*'-')
        name = data[0].strip()
        phone = data[1].strip()
        email = data[2].strip()
        address = data[3].strip()
        
        leftSpaces = int((nameWidth-len(name)-2)/2)
        print(f"|{(leftSpaces)* ' '}{name}{(nameWidth - (len(name)+leftSpaces+2))  * ' '}|",end='')

        leftSpaces = int((phoneWidth-len(phone)-2)/2)
        print(f"{(leftSpaces)* ' '}{phone}{(phoneWidth - (len(phone)+leftSpaces+2))  * ' '}|",end='')

        leftSpaces = int((emailWidth-len(email)-2)/2)
        print(f"{(leftSpaces)* ' '}{email}{(emailWidth - (len(email)+leftSpaces+2))  * ' '}|",end='')

        leftSpaces = int((addressWidth-len(address)-2)/2)
        print(f"{(leftSpaces)* ' '}{address}{(addressWidth - (len(address)+leftSpaces+2))  * ' '}|")

    print(width*'-')



#show all contacts as table
def view_all_contacts():
    with open("contacts.txt", "r") as phonebook:
        contacts = phonebook.readlines()
    table_view(contacts)
