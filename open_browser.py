import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#driver.minimize_window()
driver.get('https://www.google.com')
current_url = driver.current_url
time.sleep(10)
driver.quit()