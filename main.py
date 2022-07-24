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
import os.path
from datetime import timedelta

from db2 import Database

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

    def send(self):
        tab = self.driver.window_handles
        users = db.get_user()
        sended_users = db.sended_users()
        
        for i in range(len(users)):

            if(users[i] in sended_users):
                logger.info("Пользователь есть в базе")
                logger.info(sended_users)
                continue


            if(i % self.per_user):
                logger.info("Пауза")
                time.sleep(self.min*60)

            self.driver.switch_to.new_window('tab')
            self.driver.get(users[i])
            time.sleep(3)
            self.driver.execute_script("document.querySelector('.input-message-input').innerText = 'привет'")
            time.sleep(3)
            logger.info(str(self.driver.current_url))
            logger.info("Отправка сообщения")
            self.driver.implicitly_wait(3)
            #self.driver.execute_script("document.querySelector('.btn-send').click()")
            time.sleep(3)
            db.update_user(users[i])
            time.sleep(2)
            self.driver.close()
            self.driver.switch_to.window(tab[0])
            time.sleep(3)
            self.driver.back()
    
    def parse(self):
        group_id = db.add_group(self.url)
        self.driver.implicitly_wait(10)
        info = self.driver.find_element(By.CSS_SELECTOR, ".chat-info")
        info.click()
        self.driver.implicitly_wait(5)
        user_block = self.driver.find_element(By.CLASS_NAME, 'search-super-content-members')
        count = 100        
        for i in range(count):
            start_time = time.monotonic()
            user_block.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
            time.sleep(5)
            link = self.driver.current_url
            db.add_user(link,group_id, datetime.datetime.now(), False)
            self.driver.back()
            time.sleep(5)
            end_time = time.monotonic()
            time_format = time.strftime("%H:%M:%S", time.gmtime((end_time - start_time)*count))
            logger.info('Время до конца парсинга: {}'.format(time_format))
            

def main():
    if(not os.path.exists('SQlite_telegramm.db')):
        db.create_db()

    bot = Bot('https://web.telegram.org/k/#@ton_raffles_chat')
    bot.start_browser()
    bot.parse()
    bot.send()

if __name__ == '__main__':
    main()