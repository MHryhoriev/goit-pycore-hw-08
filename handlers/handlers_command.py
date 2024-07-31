from .handlers_error import input_error
from models import AddressBook, Record

@input_error
def add_contact(args, book: AddressBook) -> str:
    """
    Add a new contact to the address book or update an existing contact's phone number.

    Args:
        args (list): A list containing the contact name and phone number.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating the result of the operation.
        
    Raises:
        ValueError: If the number of arguments is not exactly two.
    """
    if len(args) != 2:
        raise ValueError("Invalid number of arguments. Provide exactly two arguments: name and phone.")

    name, phone, *_ = args
    record = book.find(name)

    if record is None:
        record = Record(name)
        message = book.add_record(record)
    else:
        message = "Contact already exists."

    if phone:
        record.add_phone(phone)

    return message


@input_error
def change_contact(args, book: AddressBook) -> str:
    """
    Change the phone number for an existing contact.

    Args:
        args (list): A list containing the contact name, old phone number, and new phone number.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating the result of the operation.
        
    Raises:
        ValueError: If the number of arguments is not exactly three.
    """
    if len(args) != 3:
        raise ValueError("Invalid number of arguments. Provide exactly three arguments: name, old_phone, new_phone.")

    name, old_phone, new_phone = args
    record = book.find(name)

    if record:
        return record.edit_phone(old_phone, new_phone)
    return f"Contact with name '{name}' is missing."


@input_error
def show_phone(args, book: AddressBook) -> str:
    """
    Show the phone numbers for a specific contact.

    Args:
        args (list): A list containing one contact name.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message with the phone numbers for the contact, or an error message if the contact is not found.
        
    Raises:
        ValueError: If the number of arguments is not exactly one.
    """
    if len(args) != 1:
        raise ValueError("Invalid number of arguments. Provide exactly one contact name.")
    
    name = args[0]
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    phones = [phone.value for phone in record.phones]
    if not phones:
        return f"No phone numbers found for contact '{name}'."
    
    return f"Phone numbers for {name}: {', '.join(phones)}"


@input_error
def show_all_contacts(book: AddressBook) -> str:
    """
    Show all contacts in the address book.

    Args:
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A list of all contacts in the address book or a message if no contacts are available.
    """
    if not book.data:
        return "No contacts available."
    
    contact_list = "\n".join(str(record) for record in book.values())
    return f"Contacts:\n{contact_list}"


@input_error
def add_birthday(args, book: AddressBook) -> str:
    """
    Add or update the birthday for a contact.

    Args:
        args (list): A list containing the contact name and birthday.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message indicating the result of the operation.
        
    Raises:
        ValueError: If the number of arguments is not exactly two.
    """
    if len(args) != 2:
        raise ValueError("Invalid number of arguments. Provide exactly two arguments: name and birthday.")

    name, birthday = args
    if not name or not birthday:
        return "Name and birthday cannot be empty."

    record = book.find(name)
    if record is None:
        return f"Contact with name '{name}' is missing."

    return record.add_birthday(birthday)


@input_error
def show_birthday(args, book: AddressBook) -> str:
    """
    Show the birthday for a specific contact.

    Args:
        args (list): A list containing one contact name.
        book (AddressBook): An instance of the AddressBook class.

    Returns:
        str: A message with the birthday for the contact, or an error message if the contact is not found or the birthday is not set.
        
    Raises:
        ValueError: If the number of arguments is not exactly one.
    """
    if len(args) != 1:
        raise ValueError("Invalid number of arguments. Provide exactly one contact name.")

    name, *_ = args

    if not name:
        return "Name cannot be empty."
    
    record = book.find(name)

    if record is None:
        return f"Contact with name '{name}' is missing."
    
    if record.birthday is None:
        return f"Birthday for contact '{name}' has not been set."

    return f"{name}'s birthday is on {record.birthday}"


@input_error
def birthdays(book: AddressBook) -> str:
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "No upcoming birthdays within the next 7 days."
    
    birthday_list = "\n".join(
        f"{entry['contact_name']}: {entry['congratulation_date']}" for entry in upcoming_birthdays
    )
    
    return f"Upcoming birthdays:\n{birthday_list}"
