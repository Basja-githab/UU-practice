from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select

file = open("log_m14_6.txt", "w")

def setup_driver(xpatch):
    option = webdriver.ChromeOptions()
    option.add_experimental_option(name='detach',
                                   value=True)  # чтобы окно не закрывалось
    driv = webdriver.Chrome(options=option)
    driv.get(xpatch)                            # Переход на сайт
    driv.maximize_window()                      # Максимизация окна
    sleep(1)
    return driv

def login():
    # Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)                  # Ввод имени пользователя
    file.write("Success write login\n")         # Запись в лог
    # Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)               # Ввод пароля
    file.write("Success write password\n")      # Запись в лог
#   sleep(2)
    # Поиск кнопки входа и клик по ней
    login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_button.click()
    file.write("Success click butten-login\n")  # Запись в лог

driver = setup_driver('http://www.saucedemo.com/')
login()
# выбор опции из drop-down списка по тексту  "Price (low to high)"
# есть элемент select - используем класс Select
select = Select(driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select'))
sleep(2)
select.select_by_visible_text("Price (low to high)")
sleep(1)
driver.quit()                                     # Завершение роаботы с драйвером
file.close()

driver = setup_driver('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
# выбор опции из списка через send_keys и нажатие клавиш
click_drop = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span')
click_drop.click()
sleep(2)
click_form = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
click_form.send_keys('Denmark')
click_form.send_keys(Keys.ENTER)
sleep(3)
driver.quit()                                     # Завершение роаботы с драйвером
