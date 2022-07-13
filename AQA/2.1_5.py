from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    option = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option.click()
    option = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
