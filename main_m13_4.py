from datetime import datetime
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import datetime

file = open("sc_real_login\\log_m13_4.txt", "w")                     # Открываем файл для записи логов
#driver = webdriver.Chrome()                    # Инициализация драйвера Chrome
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True) # добавляет экспериментальный параметр к настройкам браузера
#option.add_argument("--headless")              # Добавление параметра к настройкам options для веб-драйвера
driver = webdriver.Chrome(options=option)

# end of setup
#------------------------- SC Functions ------------------------------------------
def set_up():
    driver.get('http://www.saucedemo.com/')     # Переход на сайт
    driver.maximize_window()                    # Максимизация окна

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
#   sleep(5)

def login_with_enter():
    # Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)  # Ввод имени пользователя
    file.write("Success write login\n")
    # Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)  # Ввод пароля
    file.write("Success write password\n")
    #   sleep(2)
    user_pass.send_keys(Keys.ENTER)             # Нажатие на кнопку Enter
    file.write("Success click Enter login\n")
#   sleep(5)

def fake_login():
    # Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)                  # Ввод имени пользователя
    file.write("Success write login\n")         # Запись в лог
    # Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce1"
    user_pass.send_keys(password)               # Ввод пароля
    file.write("Success write fake password\n") # Запись в лог

    # Поиск кнопки входа и клик по ней
    login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_button.click()
    file.write("Success click butten-login\n")  # Запись в лог

def refresh_page():                             # Обновление страницы
    driver.refresh()

#------------------------- END of SC Functions ------------------------------------------

#--------------------------- TESTS -----------------------------------------------------------
def test_login_redirect():                      # Проверка перехода на нужную страницу
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct():      # Проверка правильность контекста после входа в систему
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    # print(datetime.datetime.now())
    driver.save_screenshot(f"sc_real_login\\screen_test_context_after_login_is_correct_"
                           f"{datetime.datetime.now().strftime('%H.%M.%S-%Y.%m.%d')}.png")
    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")

def test_fake_login_label():                    # Проверка сообщения при вводе некорректного пароля
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, "test_fake_login_label is Failed"
    file.write("test_fake_login_label is OK \n")

#-------------------------- END OF TESTS -------------------------------------------------------
# main block
def sc_real_login():
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_with_enter():
    set_up()
    login_with_enter()

    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
 #   sleep(2)
 #   refresh_page()

    test_fake_login_label()
#------------------------------------------------------------------------------------------

#sc_fake_login()
sc_real_login()
#sc_real_login_with_enter()

# set_up()
# user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
# login = "standard_user"
# user_name.send_keys(login)                      # Ввод имени пользователя
# sleep(2)
# #user_name.send_keys(Keys.BACKSPACE)            # Удаляет символ
# user_name.send_keys(Keys.CONTROL + 'a')         # Выделяет текст

file.close()                                    # Закрытие файла
#driver.quit()                                   # Завершение роаботы с драйвером







