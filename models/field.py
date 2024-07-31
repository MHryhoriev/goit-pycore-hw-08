"""
This module defines the `Field` class and its subclasses `Name`, `Phone`, and `Birthday`.
"""

import re
from datetime import datetime

class Field:
    """
    A base class for different types of fields.

    Attributes:
        value (str): The value stored in the field.

    Methods:
        __init__(value): Initializes the field with a value.
        __str__(): Returns the string representation of the field's value.
    """

    def __init__(self, value):
        """
        Initialize the field with a value.

        Args:
            value (str): The value to store in the field.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the field's value.

        Returns:
            str: The string representation of the field's value.
        """
        return str(self.value)


class Name(Field):
    """
    Class representing a contact's name.

    Inherits from `Field`.

    This class does not add any additional functionality to `Field` but is used
    for type distinction and future extension.
    """
    pass


class Phone(Field):
    """
    Class representing a phone number.

    Inherits from `Field`.

    Attributes:
        value (str): The phone number, validated to ensure it contains exactly 10 digits.

    Methods:
        __init__(value: str): Initializes the Phone instance with validation.
        validate_phone(value: str) -> str: Validates the phone number format.
    """

    def __init__(self, value: str):
        """
        Initialize a Phone instance with validation.

        Args:
            value (str): The phone number to initialize.

        Raises:
            ValueError: If the phone number is invalid.
        """
        self.value = self.validate_phone(value)

    def validate_phone(self, value: str) -> str:
        """
        Validate the phone number format.

        Args:
            value (str): The phone number to validate.

        Returns:
            str: The validated phone number.

        Raises:
            ValueError: If the phone number is invalid. Phone number must contain exactly 10 digits.
        """
        phone_pattern = re.compile(r'^\d{10}$')
        
        if not phone_pattern.match(value):
            raise ValueError(f"Invalid phone number: {value}. Phone number must contain exactly 10 digits.")

        return value

class Birthday(Field):
    """
    Class representing a birthday.

    Inherits from `Field`.

    Attributes:
        value (datetime): The date of the birthday, parsed from a string.

    Methods:
        __init__(value: str): Initializes the Birthday instance with a date string.
        parse_birthday(value: str) -> datetime: Parses the date string and returns a datetime object.
    """

    def __init__(self, value: str):
        """
        Initialize the Birthday instance with a date string.

        Args:
            value (str): The date in DD.MM.YYYY format.

        Raises:
            ValueError: If the date format is invalid.
        """
        self.value = self.parse_birthday(value)
    
    def parse_birthday(self, value: str) -> datetime.date:
        """
        Parses the date string and returns a datetime object.

        Args:
            value (str): The date in DD.MM.YYYY format.

        Returns:
            datetime: The parsed date.

        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            return datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
