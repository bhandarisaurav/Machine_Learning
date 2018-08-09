from selenium import webdriver
import time
from datetime import datetime
from easygui import *

startTime = datetime.now()
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get("https://facebook.com")
time.sleep(10)
driver.get("https://esewa.com")

inputs = driver.find_elements_by_tag_name('input')
username = inputs.pop()
password = inputs.pop()

username.send_keys("9843500114")
password.send_keys("hello")

form = driver.find_element_by_tag_name('button')
form.click()

