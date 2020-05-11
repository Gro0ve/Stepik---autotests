from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first = browser.find_element_by_name("firstname")
    first.send_keys("Borat")

    second = browser.find_element_by_name("lastname")
    second.send_keys("Boratovich")

    email = browser.find_element_by_name("email")
    email.send_keys("123@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  

    vf = browser.find_element_by_id("file")
    #vf.click()
    vf.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


