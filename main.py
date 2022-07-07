from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re

class Bot:

    def __init__(self, url):
        host = '62.113.106.227'
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "101.0",
            "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
            }
        }
        self.url = url
        self.driver = webdriver.Remote(command_executor=f'http://{host}:4444/wd/hub', desired_capabilities=capabilities)

    def start_browser(self):
        self.driver.get(self.url)
        time.sleep(30)

    def parse(self):
        f = open('users.txt', 'w')
        self.driver.implicitly_wait(10)
        info = self.driver.find_element(By.CSS_SELECTOR, ".chat-info")
        info.click()
        self.driver.implicitly_wait(5)
        users = self.driver.find_element(By.CLASS_NAME, 'search-super-content-members')
        for i in range(5):
            users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
            tab = self.driver.window_handles
            link = self.driver.current_url
            print(link, tab)
            time.sleep(5)
            self.driver.switch_to.new_window('tab')
            print('windows-open')
            time.sleep(5)
            print('switch to new windows')
            time.sleep(5)
            self.driver.get(link)
            print('get link')
            time.sleep(5)
            self.driver.execute_script("document.querySelector('.input-message-input').innerText = 123")
            print('inner text')
            time.sleep(5)
            self.driver.implicitly_wait(3)
            time.sleep(5)
            self.driver.execute_script("document.querySelector('.btn-send').click()")
            print('click to send')
            time.sleep(5)
            f.write(self.driver.current_url + '\n')
            self.driver.close()
            self.driver.switch_to.window(tab[0])
            self.driver.back()

            time.sleep(3)
        f.close()

    def send_text(self):
        for line in open('users.txt'):
            self.driver.execute_script("window.open()")
            tab = self.driver.window_handles
            self.driver.switch_to.window(tab[-1])
            self.driver.get(line)
            #self.driver.get(line)
            time.sleep(3)
            self.driver.execute_script("document.querySelector('.input-message-input').innerText = 123")
            self.driver.implicitly_wait(3)
            self.driver.execute_script("document.querySelector('.btn-send').click()")
            time.sleep(3)
            


st = Bot('https://web.telegram.org/k/#@webpack_ru')
st.start_browser()
st.parse()
#st.send_text()