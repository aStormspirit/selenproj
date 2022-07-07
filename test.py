from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

def send_text():
    for line in open('users.txt'):
        driver.get(line)
        time.sleep(20)
        driver.execute_script("document.querySelector('.input-message-input').innerText = 123")
        driver.implicitly_wait(3)
        driver.execute_script("document.querySelector('.btn-send').click()")
        time.sleep(2)

#drop = driver.find_element(By.CLASS_NAME, 'modal-content')
#button = drop.find_element(By.CLASS_NAME, 'Button')
#button.click()
#driver.implicitly_wait(5)
#devinp = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[4]/div/div[1]/div/div[8]/div[1]')
#driver.implicitly_wait(5)
#devinp.send_keys('123')
#devinp.send_keys(Keys.ENTER)

send_text()

'''
driver = webdriver.Firefox()
driver.get("https://web.telegram.org/k/#777000")
time.sleep(20)
driver.refresh()
driver.implicitly_wait(10)
time.sleep(10)
driver.execute_script("document.querySelector('.input-message-input').innerText = 123")
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[4]/div/div[5]/button/div')
button.click()
'''