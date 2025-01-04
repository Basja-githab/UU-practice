from datetime import datetime
from itertools import count
from os import close
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains               # для перехода к конкретному блоку
from time import sleep
from selenium.common.exceptions import NoSuchElementException                  #импортируем исключение
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------- Functions ------------------------------------------
def set_up():
    driver.get('https://www.saucedemo.com')                                    # Переход на сайт
#    driver.maximize_window()                                                  # Максимизация окна

def login():
    try:
        # Поиск поля для ввода имени пользователя
        user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        login = "standard_user"
        user_name.send_keys(login)                                             # Ввод имени пользователя
        file.write("Success write login\n")                                    # Запись в лог
        # Поиск поля для ввода пароля
        user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
        password = "secret_sauce"
        user_pass.send_keys(password)                                          # Ввод пароля
        file.write("Success write password\n")                                 # Запись в лог
        sleep(2)
        # Поиск кнопки входа login и клик по ней
        login_button = driver.find_element(By.XPATH, '//input [@id="login-button"]')
        login_button.click()
        file.write("Success click button-login\n")                             # Запись в лог
        sleep(2)
        # Явное ожидание загрузки страницы
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
    except Exception as e:
        print(f"Ошибка при входе в аккаунт: {e}")

def logout():
    try:
        menu_button = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        menu_button.click()
        sleep(1)
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        sleep(2)
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/'))
    except Exception as e:
        print(f"Ошибка при выходе из аккаунта: {e}")

def number_on_the_basket_icon():                                               # цифра на значке корзины
    try:
        badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        #print(f"=badge=========={badge}")
        return badge
    except Exception as e:
        print(f"Ошибка при поиске цифры на значке корзины: {e}")

def get_products(class_name):                                                  # получить список товаров
    # найти все товары
    try:
        g_products = driver.find_elements(By.CLASS_NAME, class_name)
        product_list = []
        # enumerate нумерует список товаров и получаем кортежи (индекс и товар)
        for index, product in enumerate(g_products):
            # бежим по кортежам и распаковываем их, добавляем стоимость, получаем список кортежей
            product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text   # наименование товара
            product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text # стоимость товара
            product_list.append((index + 1, product_name, product_price))
        return product_list
    except Exception as e:
        print(f"Ошибка при получении списка товаров: {e}")

def  get_select_product():                                 # получить список номеров выбранных товаров
    selected_products = []                                 # пустой список номеров выбранных товаров
    while len(selected_products) <= len(products):
        try:
            if len(selected_products) == len(products):
                break
            product_index = int(input("Введите номер товара для добавления в корзину (или 0 для завершения): "))
            if product_index == 0:
                break
            elif product_index < 0:
                print("Номер товара < 0")
                continue
            elif product_index > len(products):
                print("Нет такого номера товара")
                continue
            if product_index in selected_products:
                print("Этот номер товара уже выбран. Введите другой номер товара")
            else:
                # добавление в корзину по номеру товара
                add_products = driver.find_elements(By.CLASS_NAME, "inventory_item")
                add_products[product_index - 1].find_element(By.CLASS_NAME, "btn_inventory").click()
                selected_products.append(product_index)    # добавление в список номеров выбранных товаров
                # print(selected_products)
        except ValueError as e:
            print("Ошибка ввода:", e)
    if selected_products:  # список выбранных номеров товаров не пуст
        return selected_products
    else:
        print("Вы ничего не выбрали")

def placing_an_order():                                                                  # Оформление заказа
    sleep(3)
    try:
        # Запрос данных пользователя
        first_name = input("Введите имя (Например, Иван или Ivan): ")
        last_name = input("Введите фамилию (Например, Иванов или Ivanov): ")
        zip_code = input("Введите почтовый код:(цифры) ")
        sleep(1)
        # ввод данных пользователя
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(first_name)
        file.write("Success write first-name\n")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(last_name)
        file.write("Success write last-name\n")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(zip_code)
        file.write("Success write postal-code\n")
        file.write("Вводимые данные на сайте не проверяются\n")
    except ValueError as e:
        print("Ошибка ввода при оформлении заказа:", e)

def order_information():                                                       # Информация о заказе
    sleep(3)
    try:
        sauce_card = driver.find_element(By.CLASS_NAME, "summary_value_label").text
        print(f"Заказ номер: {sauce_card[9:]}")

        shipping = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[4]').text
        print(f"Информация о доставке: {shipping}")

        item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
        print(f"Сумма позиций покупки: {item_total[11:]}")

        total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
        print(f"Общая стоимость покупки: {total[7:]}")
        return float(item_total[13:])
    except Exception as e:
        print(f"Ошибка при выводе информации о заказе: {e}")

def order_confirmation():                                                      # Подтверждение заказа
    sleep(1)
    order_number = driver.find_element(By.CLASS_NAME, "complete-header").text  # сообщение - Спасибо за ваш заказ!
    print(f"Заказ успешно подтвержден: {order_number}")

#------------------------- END of Functions ------------------------------------------
def test_login_redirect():                       # Проверка перехода на нужную страницу
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct():       # Проверка правильность контекста после входа в систему
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")

def  test_quantity_one_product_in_basket():      # Проверка количества штук одного товара в корзине
    # Найти все кнопки "Добавить в корзину"
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_primary")
    # Кликнуть по каждой кнопке
    button_text = []
    for button in add_to_cart_buttons:
        button_text.append(button.text)
        #print(f"Кнопка с текстом: '{button_text}'")
        button.click()
    # После клика на кнопки "Добавить в корзину" на них появляется надпись "Удалить"
    # Найти все кнопки "Удалить"
    add_to_cart_buttons_click = driver.find_elements(By.CLASS_NAME, "btn_secondary")
    button_click_text = []
    for button in add_to_cart_buttons_click:
        button_click_text.append(button.text)
        #print(f"Кнопка с текстом после click: '{button_click_text}'")
    for button in add_to_cart_buttons_click:     # вернуть кнопки в начальное состояние
        button.click()
    if button_text == button_click_text:  # текст на кнопках остался 'Add to cart' ?
        return 1
    else:
        file.write("В корзину можно положить любой товар в количестве только 1-й штуки! \n")
        return 0

def test_equals_number(number1, number2, text): # проверка совпадения цифр
    assert number1 == number2, "test_equals_number is Failed"
    file.write("test_equals_number is OK - ")
    file.write(f"{text}\n")
    if number1 == number2:
        return 1

def test_cart_redirect():                        # Проверка перехода на страницу корзины
    correct_url = "https://www.saucedemo.com/cart.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_cart_redirect is Failed"
    file.write("test_cart_redirect is OK\n")

def test_context_after_cart_is_correct():        # Проверка правильность контекста на странице корзины
    correct_text = "Your Cart"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_cart_is_correct is Failed"
    file.write("test_context_after_cart_is_correct is OK \n")

def test_comparison_list_product():    # проверка совпадения списков выбранных товаров и товаров в корзине
    assert prod_in_cart == sel_products, "test_comparison_list_product is Failed"
    file.write("test_comparison_list_product is OK\n")

def test_checkout_redirect():                    # Проверка перехода на страницу оформления товара
    correct_url = "https://www.saucedemo.com/checkout-step-one.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_checkout_redirect is Failed"
    file.write("test_checkout_redirect is OK\n")

def test_context_after_checkout_is_correct():    # Проверка правильность контекста на странице оформления товара
    correct_text = "Checkout: Your Information"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_checkout_is_correct is Failed"
    file.write("test_context_after_checkout_is_correct is OK \n")

def test_continue_redirect():                    # Проверка перехода на страницу информации о заказе
    correct_url = "https://www.saucedemo.com/checkout-step-two.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_continue_redirect is Failed"
    file.write("test_continue_redirect is OK\n")

def test_context_continue_is_correct():          # Проверка правильность контекста на странице информации о заказе
    correct_text = "Checkout: Overview"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_continue_is_correct is Failed"
    file.write("test_context_after_continue_is_correct is OK \n")

def test_finish_redirect():                      # Проверка перехода на страницу завершения заказа
    correct_url = "https://www.saucedemo.com/checkout-complete.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_finish_redirect is Failed"
    file.write("test_finish_redirect is OK\n")

def test_context_after_finish_is_correct():      # Проверка правильность контекста на странице завершения заказа
    correct_text = "Checkout: Complete!"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text == current_text.text, "test_context_after_finish_is_correct is Failed"
    file.write("test_context_after_finish_is_correct is OK \n")

def test_logout_redirect():                     # проверка выхода на нужную страницу после logout
    correct_url = 'https://www.saucedemo.com/'
    get_url = driver.current_url
    assert correct_url == get_url, "test_logout_redirect is Failed"
    file.write("test_logout_redirect is OK \n")

def test_context_after_logout_is_correct():      # Проверка правильность контекста после выхода
    correct_text = "Accepted usernames are:"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_credentials"]/h4')
    assert correct_text == current_text.text, "test_context_after_logout_is_correct is Failed"
    file.write("test_context_after_logout_is_correct is OK \n")

#-------------------------- END OF TESTS -------------------------------------------------------
def sc_real_login():
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()

def sc_go_to_cart():
    try:
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()  # click на значок корзины
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/cart.html'))
    except Exception as e:
        print(f"Ошибка при переходе на страницу корзины - Your Cart: {e}")

    test_cart_redirect()
    test_context_after_cart_is_correct()

def sc_go_to_checkout():
    try:
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()  # click на кнопку checkout
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/checkout-step-one.html'))
    except Exception as e:
        print(f"Ошибка при переходе на страницу оформления товара - Checkout: Your Information: {e}")

    test_checkout_redirect()
    test_context_after_checkout_is_correct()

def sc_go_to_continue():
    try:
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()  # click на кнопку continue
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/checkout-step-two.html'))
    except Exception as e:
        print(f"Ошибка при переходе на страницу информации о заказе - Checkout: Overview: {e}")

    test_continue_redirect()
    test_context_continue_is_correct()

def sc_go_to_finish():
    try:
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()  # click на кнопку finish
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/checkout-complete.html'))
    except Exception as e:
        print(f"Ошибка при переходе на страницу завершения заказа - Checkout: Complete!: {e}")

    test_finish_redirect()
    test_context_after_finish_is_correct()

def sc_logout():
    logout()

    test_logout_redirect()
    test_context_after_logout_is_correct()
#--------------------------------  END of SC Functions -------------------------------------------
try:
    file = open("log_m14_9_tz.txt", "w", encoding = 'utf-8' )                      # Открываем файл для записи логов
    option = webdriver.ChromeOptions()
    option.add_experimental_option(name='detach', value=True) # добавляет экспериментальный параметр к настройкам браузера
    #option.add_argument("--headless")               # Добавление параметра к настройкам options для веб-драйвера
    driver = webdriver.Chrome(options=option)        # Инициализация драйвера Chrome

    sc_real_login()                                                                # ввод логина и пароля

    products = get_products("inventory_item")                                      #  получение списка товаров
    print("Список товаров:")
    for index, name, price in products:
        print(f"{index}. {name} - {price}")

    # тест на проверку количества штук одного товара в корзине
    if test_quantity_one_product_in_basket() != 1:
        print(f"Внимание! В корзину можно положить любой товар в количестве только 1-й штуки!")

    # Ввод товаров, которые хочет купить пользователь
    n_sel_products = get_select_product()                                          # список выбранных номеров товаров

    if n_sel_products:                                                             # если товар выбран
        print("Вы добавили в корзину следующие товары:")
        price_sel_products = 0
        sel_products = []
        i = 1
        for index in n_sel_products:
            product_name = products[index - 1][1]
            price_sel_products += float(products[index - 1][2].replace('$', ''))   # общая стоимость выбранных товаров
            #print(f"{product_name} ")
            sel_products.append((i, product_name, products[index - 1][2]))
            i +=1
        for i, name, price in sel_products:
            print(f"{i}. {name} - {price}")

        print(f"Количество выбранных товаров - {len(n_sel_products)}, сумма позиций покупки - {price_sel_products}")
        count_icon_cart = int(number_on_the_basket_icon())                         # цифра на значке корзины
        # тест на совпадение количества выбранных товаров с цифрой на корзине
        test_equals_number(len(n_sel_products), count_icon_cart, "кол-во выбранных товаров и цифра на значке корзины")

        sc_go_to_cart()                                                            # переход на страницу корзины
        sleep(2)
        prod_in_cart = get_products("cart_item")                                   # список товаров в корзине
        print("Список товаров в корзине:")
        for index, name, price in prod_in_cart:
            print(f"{index}. {name} - {price}")

        # тест на совпадение количества товаров в корзине с цифрой на корзине
        test_equals_number(len(prod_in_cart), count_icon_cart,"кол-во товаров в корзине и цифра на значке корзины")

        # тест на совпадение количества выбранных товаров c количеством товаров в корзине
        if test_equals_number(len(prod_in_cart),len(sel_products), "кол-во товаров в корзине"
                                                                   " и кол-во выбранных товаров"):
            test_comparison_list_product()
        # Если в корзине один товар и нажали кнопку Remove, кнопка Checkout д.б. блокирована, а кнопка
        # Continue Shopping д.б. зеленого цвета
        # Нажатие на кнопку Checkout и переход на страницу оформления заказа
        if count_icon_cart != 0:
            sc_go_to_checkout()
            # Оформление заказа
            placing_an_order()
            # Нажатие на кнопку Continue и переход на страницу информации о заказе
            sc_go_to_continue()
            # Информация о заказе
            total_price_position = order_information()
            test_equals_number(price_sel_products, total_price_position, "общая стоимость выбранных товаров и "
                                                                     "сумма позиций товаров в заказе")
            # Нажатие на кнопку finish и переход на страницу подтверждения заказа
            sc_go_to_finish()
            # Подтверждение заказа
            order_confirmation()
        else:
            print("Из корзины удалили все товары. Чтобы продолжить покупки нажмите 'Continue Shopping' ")
            file.write("Из корзины удалили все товары")

    # Выход из аккаунта
    sc_logout()
    file.close()
    sleep(2)
    driver.quit()                                                                  # Завершение работы с драйвером

except Exception as e:
    print(f"Ошибка при выполнении основного кода: {e}")
finally:
    driver.quit()
    if 'file' in locals(): # Если переменная file ещё существует
        file.close()
