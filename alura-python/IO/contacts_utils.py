import csv
import json
import pickle
from contact import Contact


def csv_to_contacts(path, encoding="latin_1"):
    contacts = []

    with open(path, encoding=encoding) as file:
        reader = csv.reader(file)
        for id, name, email in reader:
            contact = Contact(id, name, email)
            contacts.append(contact)

    return contacts


def contacts_to_pickle(contacts, path):
    with open(path, mode="wb") as file:
        pickle.dump(contacts, file)


def pickle_to_contacts(path):
    with open(path, mode="rb") as file:
        contacts = pickle.load(file)
    return contacts


def contacts_to_json(contacts, path):
    with open(path, mode="w") as file:
        # using internal var and function to convert to dict
        # json.dump(contacts, file, default=_contact_to_json)

        # using lambda to conversion to dict
        json.dump(contacts, file, default=lambda contato: contato.__dict__)


def _contact_to_json(contact):
    return contact.__dict__


def json_to_contacts(path):
    contacts = []
    with open(path) as file:
        contacts_json = json.load(file)
        for contact in contacts_json:
            # c = Contact(contact['id'], contact['name'], contact['email'])
            c = Contact(**contact)
            contacts.append(c)
    return contacts
