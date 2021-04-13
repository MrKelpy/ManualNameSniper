# encoding: utf-8

# Created at 09/04/2021
__license__ = "GNU General Public License v3.0"
__author__ = "Alexandre Silva // MrKelpy"
__copyright__ = "© Alexandre Silva 2021"

# Builtin Imports
import os
import sys
import time

# Third-Party Imports
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Local application imports
from get_credentials import EMAIL, PASSWORD, TARGET
from get_username_drop import check_availability, wait_for_drop
from LaminariaCore import *

# Options and settings
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "../resources", "chromedriver.exe")
LOGIN_URL = "https://www.minecraft.net/en-us/login"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36")


# Locking Mechanism
def lock():

    while True:
        time.sleep(60*60)


# Logging Function
def log(message: str):

    """
    Logs a message to the console
    :param message:
    :return:
    """

    print(f"[{get_formatted_date_now(include_seconds=True)}] {message}")


if not check_availability(TARGET):
    log("That name is not available! Choose another one and try again!")
    time.sleep(5)
    sys.exit()


with Chrome(CHROMEDRIVER_PATH, options=options, service_log_path=os.devnull) as driver:

    """
    Chrome instance used to send instructions to a controlled browser
    Browser: Chromium
    Driver: Chromedriver
    """

    driver.get(LOGIN_URL)
    driver.implicitly_wait(60*5)
    log(f"URL: {LOGIN_URL}")
    driver.maximize_window()

    # Gather login fields
    log("Gathering login and password fields")
    email = driver.find_element_by_id("emailField")
    password = driver.find_element_by_id("password")

    # Input login credentials
    log("Inputting login information")
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    email.submit()

    # Pauses the program incase of a captcha
    input("Program paused - Solve the captcha! (If there's none, ignore it.) Press ENTER in the terminal to continue.")

    # Checks if the credentials are wrong
    try:
        driver.implicitly_wait(1)
        _ = driver.find_element_by_id("emailField")
        driver.close()
        log("Wrong credentials! Review them and try again.")
        time.sleep(5)
        sys.exit()

    except:
        driver.implicitly_wait(60*5)
        driver.maximize_window()

    # Waits until the right time, and then changes the username automatically
    if not wait_for_drop(TARGET):
        log("This name is not available! Choose another name and try again.")

    else:

        driver.find_element_by_tag_name("html").send_keys(Keys.F5)

        primary_namechange = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div[5]/div[1]/dl/dd/button")
        _ = primary_namechange.location_once_scrolled_into_view

        time.sleep(0.5)
        primary_namechange.click()

        new_name_input = driver.find_element_by_id("newName")
        _ = new_name_input.location_once_scrolled_into_view
        new_name_input.send_keys(TARGET)

        new_name_input.submit()
        log("Name change attempted. Check https://minecraft.net to verify the success!")
        time.sleep(5)
