from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    #link1 = "http://suninjuly.github.io/redirect_accept.html"
    #browser.get(link1)

    button1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button1.click()

    #browser.switch_to.window("http://suninjuly.github.io/redirect_page.html?")
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #confirm = browser.switch_to.alert
    #confirm.accept()

    q = browser.find_element_by_id("input_value")
    w = q.text
    x = int(w)
    y = calc(x)
    r = str(y)

    sv = browser.find_element_by_id("answer")
    sv.send_keys(r)

    button2 = browser.find_element_by_class_name("btn.btn-primary")
    button2.click()
    

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


