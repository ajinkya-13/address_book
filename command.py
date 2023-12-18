import time
import faker
from contact import Contact  # Import the Contact class

class Command:
    def execute(self, address_book):
        pass

class AddContactCommand(Command):
    def execute(self, address_book):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        phone_number = input("Enter phone number: ")

        contact = Contact(first_name, last_name, address, phone_number)
        status = address_book.add_contact(contact)
        if status == 1:
            print("Success: Contact added")

class SearchContactCommand(Command):
    def execute(self, address_book):
        query = input("Enter name or phone number to search: ")
        start_time = time.time()
        results = address_book.search_contact(query)
        end_time = time.time()

        print(f"Search Results ({round(end_time - start_time, 6)} seconds):")
        for result in results:
            print(f"Name: {result.first_name} {result.last_name}\tAddress: {result.address}\tPhone: {result.phone_number}")

class LoadMockDataCommand(Command):
    def execute(self, address_book):
        fake = faker.Faker()
        for _ in range(2):
            first_name = fake.first_name()
            last_name = fake.last_name()
            address = fake.address()
            phone_number = int(fake.unix_time())

            contact = Contact(first_name, last_name, address, phone_number)
            address_book.add_contact(contact)
        print("Mock data loaded successfully!")
