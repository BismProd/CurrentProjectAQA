# получение ответа и автоматический его ввод на степике
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CLASS_NAME, 'btn-primary').click()
browser.switch_to.alert.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.CLASS_NAME, 'btn-primary').click()

alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]

browser.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)

browser.find_element(By.ID, 'id_login_email').send_keys('***')# здесь вводится e-mail
browser.find_element(By.ID,'id_login_password').send_keys('***')# здесь вводится пароль

browser.find_element(By.CLASS_NAME,'sign-form__btn').click()
time.sleep(3)
browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
time.sleep(3)

browser.find_element(By.CSS_SELECTOR, 'textarea')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

browser.find_element(By.CLASS_NAME, 'submit-submission')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
button.click()