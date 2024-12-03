from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()                     # Инициализация драйвера Chrome

driver.get('http://www.saucedemo.com/')         # Переход на сайт
driver.maximize_window()                        # Максимизация окна

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')

login = "standard_user"
user_name.send_keys(login)                      # Ввод имени пользователя

sleep(5)

#driver.quit()                                  # Завершение роаботы с драйвером




#name = driver.find_element(By.XPATH, "//h4[text()='Password for all users:']")
#name = driver.find_element(By.XPATH, "//h4[contains(text(),'Password for all')]")
#user_name = driver.find_element(By.ID, 'user-name')
#user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
#user_name = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')

# для driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
#button = driver.find_element(By.XPATH,'//input[@value="Check All"]')
#checkbox = driver.find_element(By.XPATH, '(//*[@class = "mr-10"])[3]')

# для driver.get('https://www.lambdatest.com/selenium-playground/table-data-download-demo')
#dt_button = driver.find_element(By.XPATH, '//span[text()="Copy"]')
