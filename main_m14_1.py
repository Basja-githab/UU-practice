from datetime import datetime
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
import datetime

#file = open("log_m14_1.txt", "w")
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True) # добавляет экспериментальный параметр к настройкам браузера
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/checkbox')        # Переход на сайт
driver.maximize_window()                         # Максимизация окна

# driver.back()                                   # двигаться <- на страницу назад
# sleep(2)
# driver.forward()                                # двигаться -> на страницу вперёд
sleep(2)
main_lits = driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
main_lits.click()                                 # клик на + , чтобы раскрыть Home
sleep(1)
home_check_box = driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
home_check_box.click()
sleep(1)
home_check_box.click()

#file.close()