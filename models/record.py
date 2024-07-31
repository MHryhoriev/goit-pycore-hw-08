"""
This module defines the `Record` class which manages contact details.
"""

from .field import Name, Phone, Birthday
from typing import Optional, List

class Record:
    def __init__(self, name: str):
        """
        Initialize the record with a name and an empty list of phones.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: str) -> None:
        """
        Add a phone number to the record.

        Args:
            phone (str): The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """
        Remove a phone number from the record.

        Args:
            phone (str): The phone number to remove.
        """
        self.phones = list(filter(lambda item: item.value != phone, self.phones))

    def edit_phone(self, old_phone: str, new_phone: str) -> str:
        """
        Edit an existing phone number in the record.

        Args:
            old_phone (str): The phone number to replace.
            new_phone (str): The new phone number.

        Returns:
            str: A message indicating the result of the operation.
        
        If the old phone number is found and replaced, returns "Phone number successfully updated."
        If the old phone number is not found, returns "Phone number not found."
        """
        phone_to_edit = next((phone for phone in self.phones if phone.value == old_phone), None)
        if phone_to_edit:
            phone_to_edit.value = Phone(new_phone).value
            return "Phone number successfully updated."
        return "Phone number not found."
    

    def find_phone(self, phone: str) -> Optional[Phone]:
        """
        Find a phone number in the record.

        Args:
            phone (str): The phone number to find.

        Returns:
            Phone or None: The phone number if found, else None.
        """
        return next((item for item in self.phones if item.value == phone), None)
    
    def add_birthday(self, birthday: str) -> str:
        """
        Add or update the birthday for the contact.

        Args:
            birthday (str): The birthday to add.

        Returns:
            str: A message indicating the result of the operation.
        
        If the birthday is successfully added, returns "Birthday successfully added!"
        If the birthday is already set, returns "Birthday already exists!"
        """
        if not self.birthday:
            self.birthday = Birthday(birthday)
            return "Birthday successfully added!"
        return "Birthday already exists!"

    def __str__(self) -> str:
        """
        Return a string representation of the record.

        Returns:
            str: A formatted string containing the contact's name, phone numbers, and birthday.
        """
        phones_str = ', '.join(p.value for p in self.phones)
        birthday_str = self.birthday.value if self.birthday else "Not set"
        return f"Name: {self.name.value}, Phones: {phones_str}, Birthday: {birthday_str}"
