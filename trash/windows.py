from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()


for i in range(3):
    driver.get('https://ru.wikipedia.org')
    driver.switch_to.new_window('tab')
    print(driver.window_handles)
    driver.get('https://web3-news.online/')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    print('help')