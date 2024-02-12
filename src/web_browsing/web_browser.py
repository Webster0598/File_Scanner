from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_login_date(file_path):

    cwd = os.getcwd()
    print("cwd: ", cwd)
    lis = []

    with open(file_path, "r") as f:

        for line in f:

            lis.append(line)

        f.close()

    res = []
    for sub in lis:
        res.append(sub.replace("\n", ""))

    print(res)

    return res

def login():
    log_data = read_login_date("login/login_data.txt")

    driver = webdriver.Edge()

    driver.get("https://www.practicefusion.com/")

    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle

    assert len(driver.window_handles) == 1

    driver.find_element(by=By.CLASS_NAME, value="topnav__login-link").click()

    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    email_input = driver.find_element(by=By.ID, value="inputUsername")
    email_input.send_keys(log_data[0])

    pswd_input = driver.find_element(by=By.ID, value="inputPswd")
    pswd_input.send_keys(log_data[1])

    login_button = driver.find_element(by=By.ID, value="loginButton")
    login_button.click()

    time.sleep(10)
    driver.quit()

def start():
    pass