from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
from datetime import datetime, timedelta

#file = open("log_m14_5.txt", "w")
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True)   # добавляет экспериментальный параметр к настройкам браузера
driver = webdriver.Chrome(options=option)

driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')     # Переход на сайт
driver.maximize_window()                                             # Максимизация окна

sleep(1)
slider = driver.find_element(By.XPATH,'//*[@id="id2"]')              # находим элемент ползунок
action = ActionChains(driver)
sleep(2)
#      нажать и зажать               сместить        отпустить выполнить
action.click_and_hold(slider).move_by_offset(-500, 0).release().perform()




#file.close()