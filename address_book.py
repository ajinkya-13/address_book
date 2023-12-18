
import json
from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = {}
        self.phone_index = {}
        self.name_index = {}

    def add_contact(self, contact):
        key = self.get_contact_key(contact)
        name = self.get_name_key(contact)
        if contact.phone_number in self.phone_index:
            print(f"Errror: Contact with phone number {contact.phone_number} already exists. Cannot add duplicate.")
            return 0

        #if query consists of an existing name, we update the contact.
        self.contacts[key] = contact
        self.phone_index[contact.phone_number] = contact
        self.name_index[name] = contact
        return 1

    def search_contact(self, query):
        query = query.lower()
        results = []

        if query.isdigit():
            if query in self.phone_index:
                results.append(self.phone_index[query])
        else:
            if query in self.name_index:
                results.append(self.name_index[query])

        return results

    @staticmethod
    def get_contact_key(contact):
        return f"{contact.first_name.lower()}_{contact.last_name.lower()}_{contact.phone_number}"

    @staticmethod
    def get_name_key(contact):
        return f"{contact.first_name.lower()}_{contact.last_name.lower()}"

    def load_data(self):
        try:
            with open("address_book.json", "r") as file:
                data = json.load(file)
                self.contacts = {key: Contact(**contact_data) for key, contact_data in data.items()}
                self.phone_index = {contact.phone_number: contact for contact in self.contacts.values()}
                self.name_index = {self.get_name_key(contact): contact for contact in self.contacts.values()}
        except FileNotFoundError:
            pass

    def save_data(self):
        data = {self.get_contact_key(contact): vars(contact) for contact in self.contacts.values()}
        with open("address_book.json", "w") as file:
            json.dump(data, file, indent=2)

        with open("phone_index.json", "w") as file:
            json.dump(list(self.phone_index.keys()), file, indent=2)

        with open("name_index.json", "w") as file:
            json.dump(list(self.name_index.keys()), file, indent=2)
