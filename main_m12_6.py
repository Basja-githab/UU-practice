from os import close
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

file = open("log_m12_6.txt", "w")               # Открываем файл для записи логов
#driver = webdriver.Chrome()                    # Инициализация драйвера Chrome
option = webdriver.ChromeOptions()
option.add_experimental_option(name='detach', value=True) # добавляет экспериментальный параметр к настройкам браузера
#option.add_argument("--headless")              # Добавление параметра к настройкам options для веб-драйвера
driver = webdriver.Chrome(options=option)
# end of setup

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

def test_login_redirect():                      # Проверка перехода на нужную страницу
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct():      # Проверка правильность контекста после входа в систему
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")

# main block
set_up()
login()

test_login_redirect()
test_context_after_login_is_correct()

file.close()                                    # Закрытие файла
#driver.quit()                                   # Завершение роаботы с драйвером

