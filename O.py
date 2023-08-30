from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get(r'http://suninjuly.github.io/explicit_wait2.html')

s = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
s.click()



x = int(browser.find_element(By.ID, 'input_value').text)
x = math.log(abs(12*math.sin(x)))
browser.find_element(By.ID, 'answer').send_keys(str(x))
browser.find_element(By.ID, 'solve').click()



time.sleep(10)

browser.quit()

