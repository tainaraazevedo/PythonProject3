import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/v1/')

# title
print("o titulo da pagina é:", browser.title)

#current_url
print("a URL pagina é:", browser.current_url)

#page_source
print("o codigo fonte da pagina  é:",browser.page_source)
