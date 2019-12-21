

contact_dictionary = {}
contact_details = []


def add_contact():
    contact_details = input("Enter contact name, phone number, email, address ").split(",")
    name = contact_details[0]
    phone = contact_details[1]
    email = contact_details[2]
    address = contact_details[3]
    contact_record = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    # Add contact record as a value to name key in the dictionary
    contact_dictionary[name] = contact_record


def search_contact():
    search_for = input("Search:")
    for x in contact_dictionary:
        if contact_dictionary[x]['Name'] == search_for:
            print ("True")
            print(contact_dictionary[x])
        elif contact_dictionary[x]['Phone'] == search_for:
            print ("True")
            print(contact_dictionary[x])
        if contact_dictionary[x]['Email'] == search_for:
            print ("True")
            print(contact_dictionary[x])
        if contact_dictionary[x]['Address'] == search_for:
            print ("True")
            print(contact_dictionary[x])

def main():
    add_contact()
    while True:
        user_input = input("Enter 1 to add more contacts, or 2 to search a contact, 3 to exit")
        if user_input == "1":
            add_contact()
        elif user_input == "2":
            search_contact()
        elif user_input == "3":
            break


if __name__ == '__main__':
    main()
