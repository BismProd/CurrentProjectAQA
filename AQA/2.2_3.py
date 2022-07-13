from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_value = browser.find_element(By.ID, 'num1')
    x = int(first_value.text)
    second_value = browser.find_element(By.ID, 'num2')
    y = int(second_value.text)

    sum_elem = str(x + y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_elem)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
