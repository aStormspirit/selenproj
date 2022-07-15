from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


profile_path = r'/home/vladimir/Рабочий стол/project/pybot/profile/'
options=Options()
options.set_preference('profile', profile_path)

driver = webdriver.Firefox(options=options)
driver.get("https://web.telegram.org/k/#@seochat")
time.sleep(20)
info = driver.find_element(By.CSS_SELECTOR, ".chat-info")
info.click()
driver.quit()