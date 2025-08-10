import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from click import command, option
import click




browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

wait = WebDriverWait(browser, 30)

browser.find_element(By.ID, "dropdown").click()
wait.until(EC.alert_is_present())
time.sleep(6)

browser.find_element(By.ID,"color-button").click()
wait.until((EC.text_to_be_present_in_element(By.XPATH,)))
time.sleep(5)
