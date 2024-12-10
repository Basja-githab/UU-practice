from datetime import datetime
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
import datetime

#file = open("log_m14_3.txt", "w")
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True)   # добавляет экспериментальный параметр к настройкам браузера
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/buttons')                     # Переход на сайт
driver.maximize_window()                                    # Максимизация окна

sleep(2)
double_click_button = driver.find_element(By.XPATH,'//*[@id="doubleClickBtn"]')  # Кнопка с двойным кликом
right_click_button = driver.find_element(By.XPATH,'//*[@id="rightClickBtn"]')    # Кнопка с правым кликом
standard_click_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')
                                                                                 # Стандартная кнопка (левый клик)
action = ActionChains(driver)                               # создаем экземпляр класса ActionChains
action.double_click(double_click_button).perform()          # двойной клик по кнопке выполнить
sleep(2)
action.context_click(right_click_button).perform()          # правый клик по кнопке выполнить
sleep(2)
standard_click_button.click()                               # стандартный (левый) клик по кнопке
#file.close()