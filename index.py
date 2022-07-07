from selenium import webdriver
from selenium.webdriver.common.by import By
import time
f = open('users.txt', 'w')


driver = webdriver.Firefox()
driver.get("https://web.telegram.org/k/#@seochat")
time.sleep(20)
info = driver.find_element(By.CSS_SELECTOR, ".chat-info")
info.click()
print(info)
driver.implicitly_wait(3)
users = driver.find_element(By.CLASS_NAME, 'search-super-content-members')
for i in range(10):
    users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
    time.sleep(2)
    f.write(driver.current_url + '\n')
    driver.back()
    time.sleep(2)