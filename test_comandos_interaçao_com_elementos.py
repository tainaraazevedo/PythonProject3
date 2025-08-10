import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.saucedemo.com/')

#find_element()
username = browser.find_element(By.ID,"user-name")
password = browser.find_element(By.ID,"password")
btn_login = browser.find_element(By.ID,"login-button")
#time.sleep()


#send_keys()
username.send_keys("standard_user")
time.sleep(5)
password.send_keys("secret_sauce")

#click()
btn_login.click()
#time.sleep()

#text()
products_title = browser.find_element(By.XPATH,"//span[@class='title']")
print(products_title.text)
assert products_title.text == "Products"
#get_attribute()
img_backpack = browser.find_element(By.XPATH,"(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"
assert img_backpack.is_displayed()







