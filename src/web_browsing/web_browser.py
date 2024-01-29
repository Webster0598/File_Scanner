from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start():

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

    print(driver.current_url)
    email_input = driver.find_element(by=By.CLASS_NAME, value="loginInput")
    print(email_input)

    time.sleep(3)
    driver.quit()