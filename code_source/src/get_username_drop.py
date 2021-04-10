# encoding: utf-8

# Created at 09/04/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# built-in imports
from datetime import datetime
import time

# Local Application imports
from namemc_interactions import get_drop_timestamp


def check_availability(target: str):

    """
    Checks the availability of a name.
    :param target: The username -> str
    :return:
    """

    drop_timestamp = get_drop_timestamp(target)

    # Checks if name is not dropping
    if not drop_timestamp:
        return 1

    return drop_timestamp


def wait_for_drop(target: str):

    """
    Blocks the program flow until the name is dropped
    :param target: The username -> str
    :return:
    """

    # Checks the availability of an username in a function for usability outside the scope of wait_for_drop
    drop_timestamp = check_availability(target)
    if not drop_timestamp:
        return False

    now = datetime.now()

    # Checks if the timestamp has already occured
    if datetime.timestamp(now) > drop_timestamp:
        return drop_timestamp

    waiting_time = drop_timestamp - datetime.timestamp(now)
    time.sleep(waiting_time)

    return drop_timestamp

