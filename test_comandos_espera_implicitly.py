import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

checkbox = browser.find_element(By.XPATH,"/html/body/div/section[4]/label[1]/input")
assert checkbox.is_displayed()
time.sleep(6)
print("checkbox na tela!")
