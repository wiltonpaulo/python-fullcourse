import contacts_utils

try:
    contacts = contacts_utils.csv_to_contacts("data/contacts.csv")
    # contacts_utils.contacts_to_pickle(contacts, "data/contacts.pickle")
    # contacts = contacts_utils.pickle_to_contacts("data/contacts.pickle")
    contacts_utils.contacts_to_json(contacts, "data/contacts.json")
    # contacts = contacts_utils.json_to_contacts("data/contacts.json")
    for contact in contacts:
        print(f"{contact.id} / {contact.name} / {contact.email}")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No write permission")
