from datetime import datetime
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
import datetime

#file = open("log_m14_2.txt", "w")
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True) # добавляет экспериментальный параметр к настройкам браузера
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/radio-button')    # Переход на сайт
driver.maximize_window()                         # Максимизация окна

sleep(1)
yes_radio = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label')
yes_radio.click()
sleep(3)

if yes_radio.is_displayed(): # возвращает `true` или `false` элемент присутствует на странице или нет
    print("YES")
else:
    print("NO")

#file.close()