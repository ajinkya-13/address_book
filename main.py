
from address_book import AddressBook
from command import AddContactCommand, SearchContactCommand, LoadMockDataCommand

def print_menu():
    print("\nAddress Book CLI:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")
    print("4. Load Mock Data")

def main():
    address_book = AddressBook()
    address_book.load_data()

    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "3":
            print("Exiting Address Book CLI. Goodbye!")
            break
        elif choice == "1":
            AddContactCommand().execute(address_book)
        elif choice == "2":
            SearchContactCommand().execute(address_book)
        elif choice == "4":
            LoadMockDataCommand().execute(address_book)
        else:
            print("Invalid choice. Please enter a valid option.")

        address_book.save_data()

if __name__ == "__main__":
    main()
