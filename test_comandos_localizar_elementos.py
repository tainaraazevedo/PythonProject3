import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")


#find_element()
#username = browser.find_element(By.ID,"user-name")
#password = browser.find_element(By.ID,"password")

#send_keys
#username.send_keys("standard_user")
#password.send_keys("secret_sauce")


#find_elements()
#username.send_keys("standard_user")
#password.send_keys("secret_sauce")

auth_fields = browser.find_elements(By.CLASS_NAME, "form_input")
print(auth_fields)
print(len(auth_fields))
assert len(auth_fields) == 2, "o numero de elementos encontrado é diferente do esperado"


time.sleep(6)