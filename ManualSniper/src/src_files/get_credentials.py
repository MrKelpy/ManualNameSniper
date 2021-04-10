# encoding: utf-8

# Created at 09/04/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# built-in imports
import os

# Local Application imports
from exceptions import NotSetupException

settings_filepath = os.path.join(os.getcwd(), "../settings.txt")

with open(settings_filepath, 'r') as settings:
    setting_lines = settings.readlines()

EMAIL = setting_lines[0][6:].strip()
PASSWORD = setting_lines[1][9:].strip()
TARGET = setting_lines[2][16:].strip()

if not EMAIL or not PASSWORD or not TARGET:

    raise NotSetupException("Fill in the settings completely before continuing!")
