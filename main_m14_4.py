from datetime import datetime
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains     # для перехода к конкретному блоку
from time import sleep
#import datetime
from datetime import datetime, timedelta

#file = open("log_m14_4.txt", "w")
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True)   # добавляет экспериментальный параметр к настройкам браузера
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/date-picker')                # Переход на сайт
driver.maximize_window()                                    # Максимизация окна

def clear_field(date):
    sleep(1)
    date.send_keys(Keys.CONTROL + 'a')
    date.send_keys(Keys.DELETE)                             # очищаем поле

def close_popup_window():
    sleep(1)
    # чтобы закрыть всплывающее окно клик по "Date Picker"
    date_picker_container = driver.find_element(By.XPATH, '//*[@id="datePickerContainer"]/h1')
    date_picker_container.click()                           # закрыть всплывающее окно

date_input = driver.find_element(By.XPATH,'//*[@id="datePickerMonthYearInput"]')
clear_field(date_input)                                     # очищаем поле Select Date
sleep(1)
current_date = datetime.now()                               # now возвращает текущее время и дату
current_date = current_date.strftime("%m.%d.%Y")
date_input.send_keys(current_date)
close_popup_window()

date_time_input = driver.find_element(By.XPATH,'//*[@id="dateAndTimePickerInput"]')
clear_field(date_time_input)                                # очищаем поле Date and Time
sleep(1)
curr_date = datetime.now()
future_date = curr_date + timedelta(days=10)                # увеличиваем текущую дату на 10 дней
#print(future_date)
future_date = future_date.strftime("%B, %d %Y %H:%M")
#print(future_date)
date_time_input.send_keys(future_date)                      # записываем в поле Date and Time
close_popup_window()

#file.close()