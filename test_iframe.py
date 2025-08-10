import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.common.by import By


browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')
