"""
This module defines the `AddressBook` class which manages multiple `Record` objects.
"""

from collections import UserDict
from .record import Record, Birthday
from datetime import datetime, timedelta
from typing import Optional, Dict, List

class AddressBook(UserDict):
    def __init__(self):
        """
        Initialize an empty address book.
        """
        super().__init__()

    def add_record(self, record: Record) -> str:
        """
        Add a new record to the address book.

        Args:
            record (Record): The record to add.

        Notes:
            Prints a confirmation message if the record is added successfully.
        """
        self.data[record.name.value] = record
        return f"Contact '{record.name.value}' added successfully."
        
        
    def find(self, name: str) -> Optional[Record]:
        """
        Find a record by name.

        Args:
            name (str): The name of the record to find.

        Returns:
            Record: The record if found.

        Raises:
            ValueError: If no record with the given name is found in the address book.
        """
        if name in self.data:
            print(f"Contact with name '{name}' was found!")
            return self.data[name]
        else:
            return None
        
        
    def delete(self, name: str) -> None:
        """
        Delete a record by name.

        Args:
            name (str): The name of the record to delete.

        Raises:
            ValueError: If no record with the given name is found in the address book.

        Notes:
            Prints a confirmation message if the record is deleted successfully.
        """
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' has been successfully deleted.")
        else:
            raise ValueError(f"Record with name '{name}' not found.")
        

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of contacts with upcoming birthdays within the next 7 days.

        Returns:
            list[dict]: A list of dictionaries, each containing the contact name and 
                        their congratulation date formatted as "DD.MM.YYYY".
        """
        today = datetime.today().date()
        end_date = today + timedelta(days=7)
        result = []

        for contact, details in self.data.items():
            birthday_field = details.birthday

            if not self.is_valid_birthday(birthday_field):
                continue

            contact_birthday = birthday_field.value

            congratulation_date = self.calculate_congratulation_date(contact_birthday, today, end_date)

            result.append({
                "contact_name": contact,
                "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
            })

        return result
    
    
    def is_valid_birthday(self, birthday_field) -> bool:
        """
        Validate if the birthday field is a proper Birthday object with a non-None value.

        Args:
            birthday_field (Optional[Birthday]): The field to validate.

        Returns:
            bool: True if valid, otherwise False.
        """
        return isinstance(birthday_field, Birthday) and birthday_field.value is not None
    
    
    def calculate_congratulation_date(self, contact_birthday: datetime.date, today: datetime.date, end_date: datetime.date) -> datetime.date:
        """
        Calculate the congratulation date based on the contact's birthday.

        Args:
            contact_birthday (datetime.date): The contact's birthday.
            today (datetime.date): Today's date.
            end_date (datetime.date): The end date of the 7-day period.

        Returns:
            datetime.date: The congratulation date, adjusted if necessary.
        """
        try:
            birthday_this_year = contact_birthday.replace(year=today.year)

            # If the birthday has already occurred this year, set it to next year
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if the birthday is within the next 7 days
            if today <= birthday_this_year <= end_date:
                return self.calculate_next_weekday(birthday_this_year)
            else:
                return birthday_this_year

        except Exception as ex:
            raise ValueError(f"Error calculating congratulation date: {ex}")
    

    def calculate_next_weekday(self, date: datetime.date) -> datetime.date:
        """
        Calculate the next weekday if the given date falls on a weekend.

        Args:
            date (datetime.date): The date to check.

        Returns:
            datetime.date: The next weekday date if the given date is a weekend, otherwise the same date.
        """

        if date.weekday() >= 5:
            return date + timedelta(days=(7 - date.weekday()))
        return date    