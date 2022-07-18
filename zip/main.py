from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import datetime
from db import Database

db = Database()
db.create_db()



class Bot:

    def __init__(self, url):
        self.url = url
        self.users = 10
        self.per_user = 2
        self.min = 1
        self.driver = webdriver.Firefox()

    def start_browser(self):
        self.driver.get(self.url)
        time.sleep(30)

    def send(self, link, tab):
        self.driver.switch_to.new_window('tab')
        self.driver.get(link)
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.input-message-input').innerText = 'привет'")
        time.sleep(2)
        print('сообщение')
        self.driver.implicitly_wait(3)
        self.driver.execute_script("document.querySelector('.btn-send').click()")
        time.sleep(2)
        db.add_user(link, self.url, datetime.datetime.now())
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(tab[0])
        time.sleep(2)
        self.driver.back()
    
    def parse(self):
        self.driver.implicitly_wait(10)
        info = self.driver.find_element(By.CSS_SELECTOR, ".chat-info")
        info.click()
        self.driver.implicitly_wait(5)
        users = self.driver.find_element(By.CLASS_NAME, 'search-super-content-members')
        for i in range(self.users):

            if(i % self.per_user):
                time.sleep(self.min*60)

            users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()

            tab = self.driver.window_handles
            link = self.driver.current_url
            time.sleep(2)
            if link in db.show_users():
                print('пользователь есть в базе')
                time.sleep(2)
                self.driver.back()
                continue

            print(link, tab)
            time.sleep(2)
            print('пользователя нету в базе')
            self.send(link, tab)
            time.sleep(2)
            


st = Bot('https://web.telegram.org/k/#@ton_raffles_chat')
st.start_browser()
st.parse()