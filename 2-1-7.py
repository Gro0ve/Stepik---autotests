from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    point1 = browser.find_element_by_id("treasure")
    z = point1.get_attribute ("valuex")
    x = z
    y = calc(x)

    pw = browser.find_element_by_id("answer")
    pw.send_keys(y)
    
    check1 = browser.find_element_by_css_selector("input.check-input#robotCheckbox")
    check1.click()

    check2 = browser.find_element_by_css_selector("input.check-input#robotsRule")
    check2.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()