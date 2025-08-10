import time

from selenium import webdriver

browser = webdriver.Chrome()

# get()
browser.get('https://google.com')

# maximize_windows()
browser.maximize_window()

# refresh()
browser.refresh()

# get()
browser.get('https://www.saucedemo.com/v1/')

time.sleep(5)

#back()
browser.back()
time.sleep(3)

#forward()
browser.forward()
time.sleep(3)

#close()
browser.switch_to.new_window("tab")
browser.close()
time.sleep(3)


#quit()
#browser.switch_to.new_window("tab")
#browser.switch_to.new_window("tab")
#time.sleep(3)
#browser.quit()
