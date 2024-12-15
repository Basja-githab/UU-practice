from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains       # для перехода к конкретному блоку
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select

from main_m14_6 import setup_driver

sleep(2)
driver = setup_driver('https://www.lambdatest.com/selenium-playground')
# на странице selenium-playground выбираем Simple Form Demo
page_simple_form = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/ul/li[34]/a')
page_simple_form.click()                                               # переход на страницу Simple Form Demo
# ввод в поле сообщения, при нажатии кнопки в label отображается введенное сообщение
form1_text = driver.find_element(By.XPATH, '//*[@id="user-message"]')
form1_label = driver.find_element(By.XPATH, '//*[@id="message"]')
form1_button = driver.find_element(By.XPATH, '//*[@id="showInput"]')
# ввод в 2 поля цифр, при нажатии кнопки в label отображается сумма введенных цифр
form2_text1 = driver.find_element(By.XPATH, '//*[@id="sum1"]')
form2_text2 = driver.find_element(By.XPATH, '//*[@id="sum2"]')
form2_label = driver.find_element(By.XPATH, '//*[@id="addmessage"]')
form2_button = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
# проверка совпадения введенного и отабраженного сообщения
form1_text.send_keys("Hello!")
form1_button.click()
assert "Hello!" == form1_label.text, 'NOT OK FORM 1'
print("FORM 1 is OK")
# проверка совпадения суммы введенных цифр и отображенного в label числа
form2_text1.send_keys(52)
form2_text2.send_keys(2)
form2_button.click()
assert 52+2 == int(form2_label.text), 'NOT OK FORM 2'
print("FORM 2 is OK")
sleep(4)

driver.back()                                                       # переход назад на страницу selenium-playground
# на странице selenium-playground выбираем iframe-demo
page_iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/ul/li[19]/a')
page_iframe.click()                                                 # переход на страницу  Simple iframe

iframe = driver.find_element(By.XPATH, '//*[@id="iFrame1"]')        # ищем iframe
driver.switch_to.frame(iframe)                                      # переключаемся внутрь iframe
lon = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]') # находим элемент внутри iframe
sleep(2)
lon.send_keys(Keys.CONTROL + 'a')                                   # помечаем текст
lon.send_keys(Keys.DELETE)                                          # удаляем
bold_button_iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]') # ищем кнопку "жирный текст"
bold_button_iframe.click()                                          # нажимаем на неё
lon.send_keys("New Message!")                                       # вводим новый "жирный" текст в iframe

sleep(3)
driver.quit()                                                       # Завершение роаботы с драйвером
