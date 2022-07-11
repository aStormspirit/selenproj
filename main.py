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
        self.driver = webdriver.Firefox()

    def start_browser(self):
        self.driver.get(self.url)
        time.sleep(30)

    
    def parse(self):
        f = open('users.txt', 'a')
        self.driver.implicitly_wait(10)
        info = self.driver.find_element(By.CSS_SELECTOR, ".chat-info")
        info.click()
        self.driver.implicitly_wait(5)
        users = self.driver.find_element(By.CLASS_NAME, 'search-super-content-members')
        for i in range(10):
            flag = False
            users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
            tab = self.driver.window_handles
            link = self.driver.current_url

            for user in open('users.txt'):
                print(user, link)
                if(user.strip() == link.strip()):
                    flag = True
                    break

            print(flag)

            if(flag):
                self.driver.back()
                continue
            
            print(link, tab)
            time.sleep(5)
            #send script
            self.driver.switch_to.new_window('tab')
            self.driver.get(link)
            #self.driver.get(line)
            time.sleep(3)
            self.driver.execute_script("document.querySelector('.input-message-input').innerText = 'Добрый день !Меня Илья зовут. Если я правильно понял, вы seo продвижением занимаетесь.Хочу обсудить вариант поработать вместе.Мы платформу запустили по поведенческим 2 года назад, используем региональные IP адреса, подстраиваемся под позицию сайта (чтобы не заходить, если Яндекс на проверку выбрасывает на 6 страницу), у всех пользователей нагуленная история (вплоть до тематик интересов).По нашей практике, сайты по 10 ключевикам за 2 месяца в топ-10 спокойно можно вывести (если это только не суперконкурентная тематика). Хочу пригласить вас на такую небольшую встречу (минут 10) в зуме или телеграмме, покажем платформу, может вам было бы интересно со своими клиентами в работе использовать. Что скажете, найдётся минут 10?' ")
            self.driver.implicitly_wait(3)
            #self.driver.execute_script("document.querySelector('.btn-send').click()")
            time.sleep(3)
            f.write(self.driver.current_url + '\n')
            #self.driver.close()
            #self.driver.switch_to.window(tab[0])
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