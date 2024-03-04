from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_login_date(file_path):

    # Reads the login data from a file specified by the file path.
    # Once read, then data is added to a list and returned.
    cwd = os.getcwd()
    print("cwd: ", cwd)
    lis = []

    with open(file_path, "r") as f:

        for line in f:

            lis.append(line)

        f.close()

    res = []

    # Remove new lines from the data
    for sub in lis:
        res.append(sub.replace("\n", ""))

    print(res)

    return res

def login():

    # Starts a web browser and attempts to log into a website using
    # log in data read from a text file.

    log_data = read_login_date("login/login_data.txt")

    driver = webdriver.Edge()
    driver.get("https://www.practicefusion.com/")

    # Waits 10 secs for page to load
    wait = WebDriverWait(driver, 10)

    # Saves the handle of the tab that is currently being worked with.
    original_window = driver.current_window_handle

    assert len(driver.window_handles) == 1

    # Clicks button to go to log in page
    driver.find_element(by=By.CLASS_NAME, value="topnav__login-link").click()

    # Waits for two tabs to be opened
    wait.until(EC.number_of_windows_to_be(2))

    # Changes the tab the driver is working with to the new tab.
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Inputs the login data
    email_input = driver.find_element(by=By.ID, value="inputUsername")
    email_input.send_keys(log_data[0])

    pswd_input = driver.find_element(by=By.ID, value="inputPswd")
    pswd_input.send_keys(log_data[1])

    # Clicks the log in button after data it inputed
    login_button = driver.find_element(by=By.ID, value="loginButton")
    login_button.click()

    # Waits 10 secs before closing the driver.
    time.sleep(10)
    driver.quit()

def start():
    pass