from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
#def calc(x):
  #return int(x)
#def calc(y):
  #return int(y)
#def calc(q):
  #return str(int(x)+int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    p1 = browser.find_element_by_id("num1")
    x = p1.text
    #z = calc(x)
    z = int(x)
    p2 = browser.find_element_by_id("num2")
    i = p2.text
    #w = calc(i)
    w = int(i)
    q = z+w
    print (q)
    q1 = str(q)
    
    #t = z + w
    #p22 = int(p2) 
    #p3 = p11+p22
    #p3=p3.text
    

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(q1)
    

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value("1")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()