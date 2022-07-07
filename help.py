#options.add_argument("user-data-dir=/home/vladimir/Рабочий стол/project")

#my_elem = driver.find_element(By.ID, "telegram-search-input")
#my_elem.clear()
#my_elem.send_keys('Saved Messages')
#driver.implicitly_wait(5)
#second_elem = driver.find_elements(By.CSS_SELECTOR, '.search-result')

## сохранить профиль браузера
'''
drop = self.driver.find_element(By.CLASS_NAME, 'modal-content')
            button = drop.find_element(By.CLASS_NAME, 'Button')
            button.click()
            self.driver.implicitly_wait(10)
            time.sleep(3)
            try:
                devinp = self.driver.find_element(By.XPATH, '//*[@id="editable-message-text"]')
            except NoSuchElementException:
                print('Эллемент не найден')
                continue

            devinp.clear()
            self.driver.implicitly_wait(5)
            time.sleep(3)
            devinp.send_keys('Привет')
            time.sleep(3)
            devinp.send_keys(Keys.ENTER)
            time.sleep(2)
'''
#profile = webdriver.FirefoxProfile('/home/vladimir/Рабочий стол/project/pybot/profile/')
#profile.set_preference("general.useragent.override", 'useragent')
#options = webdriver.FirefoxOptions()
#options.add_argument("user-data-dir=/home/vladimir/Рабочий стол/project/pybot/profile/")
#options.add_argument('--profile-directory=Profile 2')
#options.set_preference("dom.webnotifications.serviceworker.enabled", False)
#options.set_preference("dom.webnotifications.enabled", False)
'''
        original_window = self.driver.current_window_handle
        print(original_window)
        self.driver.switch_to.new_window()
        self.driver.switch_to.window()
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        #self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.new_window('window')

            users.find_elements(By.CLASS_NAME, 'chatlist-chat')[i].click()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(2)
            self.driver.execute_script("document.querySelector('.input-message-input').innerText = 'привет'")

            #self.driver.implicitly_wait(3)
            #self.driver.execute_script("document.querySelector('.btn-send').click()")
            #self.driver.implicitly_wait(3)
            self.driver.back()
            time.sleep(2)

                        driver2 = webdriver.Firefox()
            self.driver.execute_script("window.open()")
            tab = self.driver.window_handles
            print(tab, type(tab), tab[-1])
            self.driver.switch_to.window(tab[-1])
            self.driver.get(line)
            #self.driver.get(line)
            #time.sleep(3)
            #self.driver.execute_script("document.querySelector('.input-message-input').innerText = 123")
            #self.driver.implicitly_wait(3)
            #self.driver.execute_script("document.querySelector('.btn-send').click()")
            self.driver.close()
            time.sleep(3)
'''

webdriver.Remote(command_executor=f'http://{host}:4444/wd/hub', desired_capabilities=capabilities)