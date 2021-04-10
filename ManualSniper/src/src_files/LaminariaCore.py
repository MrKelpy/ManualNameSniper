"""
THIS CORE IS MERELY A LIBRARY OF SHARED CODE FOR RE-USAGE BETWEEN PROGRAMS CREATED BY:
NAME: ALEXANDRE SILVA
EMAIL: alexandresilva.coding@gmail.com
GitHub: https://github.com/MrKelpy

THE AFOREMENTIONED LIBRARY MAY AND WILL BE CHANGED MANY TIMES, AND THE FILE CURRENTLY IN THE POSSESSION OF THE READER IS ONLY
ONE OF IT'S COPIES.
USAGE OF DISCLAMINARIACORE FOR ANY PURPOSES BY OTHERS THAT ARE NOT THE AUTHOR
IS PERMITTED, ASWELL AS ITS MODIFICATION, COPY OR REPRODUCTION.

INCASE OF MODIFICATION LEAVE THIS MESSAGE INSIDE IT.
© Alexandre Silva 2021
"""

# built-in imports
from datetime import datetime


def twochars(arg):
    """
    Formats a string of two characters into the format of (0X), useful for date formatting.
    :param arg: The string
    :return: String
    """

    if len(arg) == 1:
        return f"0{arg}"

    return arg


def get_formatted_date(date: datetime, include_seconds: bool = False):
    """
    Returns a given date in the handy DD/MM/YY - HH:MM:SS format.
    :param date: The date to be formatted -> datetime.datetime
    :param include_seconds: If set to True, include seconds in the format.
    :return: String
    """

    date_string = f"{twochars(str(date.day))}/{twochars(str(date.month))}/{twochars(str(date.year))} - " \
                  f"{twochars(str(date.hour))}:{twochars(str(date.minute))}"

    if include_seconds:
        date_string += f":{twochars(str(date.second))}"

    return date_string


def get_formatted_date_now(include_seconds: bool = False, formatting: int = 1):
    """
    Returns the current date in the handy DD/MM/YY - HH:MM:SS format (default) or in the specified one.
    :param formatting: Format type -> int
    :param include_seconds: If set to True, include seconds in the format.
    :return: String
    """

    now = datetime.now()
    if formatting == 1:
        date_string = f"{twochars(str(now.day))}/{twochars(str(now.month))}/{twochars(str(now.year))} - " \
                      f"{twochars(str(now.hour))}:{twochars(str(now.minute))}"

    elif formatting == 2:
        date_string = f"{twochars(str(now.day))}.{twochars(str(now.month))}.{twochars(str(now.year))}_" \
                      f"{twochars(str(now.hour))}.{twochars(str(now.minute))}"

    else:
        date_string = f"{twochars(str(now.day))}/{twochars(str(now.month))}/{twochars(str(now.year))} - " \
                      f"{twochars(str(now.hour))}:{twochars(str(now.minute))}"

    if include_seconds:
        date_string += f":{twochars(str(now.second))}"

    return date_string
