import pickle
from models import AddressBook

def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """
    Save the address book data to a file.

    Args:
        book (AddressBook): The AddressBook instance to save.
        filename (str): The file name where the address book will be saved. Defaults to 'addressbook.pkl'.
    """
    try:
        with open(filename, "wb") as file:
            pickle.dump(book, file)
        print("The address book has been successfully saved!")
    except Exception as ex:
        print(f"An error occurred while saving the address book: {ex}")
        raise

def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """
    Load the address book data from a file.

    Args:
        filename (str): The file name from which the address book will be loaded. Defaults to 'addressbook.pkl'.

    Returns:
        AddressBook: The loaded AddressBook instance.

    Raises:
        ValueError: If the loaded data is not of type AddressBook.
    """
    try:
        with open(filename, "rb") as file:
            book = pickle.load(file)
        if not isinstance(book, AddressBook):
            raise ValueError("Loaded data is not of type AddressBook.")
        return book
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new AddressBook.")
        return AddressBook()
    except ValueError as ve:
        print(f"Value error: {ve}")
        raise
    except Exception as ex:
        print(f"An error occurred while loading the address book: {ex}")
        raise
