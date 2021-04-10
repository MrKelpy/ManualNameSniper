# encoding: utf-8

# Created at 09/04/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# built-in imports
from datetime import datetime
import requests

# Third-Party imports
from bs4 import BeautifulSoup
import isodate


def get_drop_timestamp(target: str):

    """
    Returns the drop timestamp for a certain username in minecraft.
    :param target: The username. -> str
    :return: int, None if not found or not available.
    """

    # Requests the user page html
    url = f"https://namemc.com/search?q={target}"
    data = requests.get(url)

    # Parses out the status and time of availability from the html
    soup = BeautifulSoup(data.text, "html.parser")
    information = soup.find_all(class_="col-sm-6 my-1")

    status = information[0].find_all("div")[1].text.strip()
    if status == "Available*":
        return 0

    time_available = information[2].find(id="availability-time")["datetime"]
    return datetime.timestamp(isodate.parse_datetime(time_available))
