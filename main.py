import logging
## for file logging
logger = logging.getLogger('spam_application')
file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

import time
import datetime
from db import Database

db = Database()

class Bot:

    def __init__(self, url):
        self.url = url
        self.users = 10
        self.per_user = 2
        self.min = 0
        self.driver = webdriver.Firefox()

    def start_browser(self):
        self.driver.get(self.url)
        time.sleep(30)

    def send(self, link, tab):
        #if(i % self.per_user):
        #    logger.info("Пауза")
        #    time.sleep(self.min*60)
        self.driver.switch_to.new_window('tab')
        self.driver.get(link)
        time.sleep(3)
        self.driver.execute_script("document.querySelector('.input-message-input').innerText = 'привет'")
        time.sleep(3)
        logger.info(str(self.driver.current_url))
        logger.info("Отправка сообщения")
        self.driver.implicitly_wait(3)
        #self.driver.execute_script("document.querySelector('.btn-send').click()")
        time.sleep(3)
        db.add_user(link, self.url, datetime.datetime.now())
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(tab[0])
        time.sleep(3)
        self.driver.back()
    
    def parse(self):
        self.driver.implicitly_wait(10)
        info = self.driver.find_element(By.CSS_SELECTOR, ".chat-info")
        info.click()
        self.driver.implicitly_wait(5)
        users = self.driver.find_element(By.CLASS_NAME, 'search-super-content-members')

        for i in range(self.users):

            users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
            time.sleep(5)
            link = self.driver.current_url
            db.add_user(link, self.url, datetime.datetime.now())
            self.driver.back()
            time.sleep(5)

            #tab = self.driver.window_handles
            

            #time.sleep(5)
            #if link in db.show_users():
                #logger.info(link)
                #logger.info("Пользователь есть в базе")
                #time.sleep(2)
                #self.driver.back()
                #continue

            #time.sleep(3)
            #logger.info("Пользователь нету базе")
            #self.send(link, tab)
            #time.sleep(3)
            

def main():
    db.create_db()
    st = Bot('https://web.telegram.org/k/#@webpack_ru')
    st.start_browser()
    st.parse()

if __name__ == '__main__':
    main()