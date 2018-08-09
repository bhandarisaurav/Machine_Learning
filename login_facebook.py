from selenium import webdriver
import time
from datetime import datetime
from easygui import *


def facebook_login():
    x = ynbox('Shall I continue?', 'Title', ['Yes', 'No'])
    if x:
        usr = enterbox("Enter Your Email / Phone no", 'Phone no / Email')
        print("Got your Email as : " + usr)
        pas = passwordbox("Enter Your Password:", "Enter Your password")
        print("Got your pass....")

        startTime = datetime.now()
        driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
        driver.get("http://facebook.com")
        time.sleep(3)
        username = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pass")

        username.send_keys(usr)
        password.send_keys(pas)

        form = driver.find_element_by_id("u_0_2")
        time.sleep(2)
        form.click()
        driver.get("http://facebook.com/sauravbh1")
        print("Done")
        print("\nTime taken: " + str(datetime.now() - startTime))
    print("Good Bye")


if __name__ == '__main__':
    print("------------------------------")
    print("Facebook Login System")
    print("Opening Login page...\nPlease Wait")
    print("------------------------------")
    time.sleep(1)
    facebook_login()
