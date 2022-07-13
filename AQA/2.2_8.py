from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_el = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
    name_el.send_keys('Ivan')

    surname_el = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
    surname_el.send_keys('Petrov')

    mail_el = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
    mail_el.send_keys('Ivanpetrov@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    download_elem = browser.find_element(By.ID, 'file')
    download_elem.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
