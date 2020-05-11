from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")

    y = browser.find_element_by_id("input_value")
    x = y.text
    q = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(q)  

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    #button = browser.find_element_by_css_selector("button.btn.btn-primary")
    #browser.execute_script("window.scrollBy(0, 100);")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


