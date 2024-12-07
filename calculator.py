def calc():
    try:
        num1 = int(input("Калькулятор работает с целыми числами"+ '\n'+ "Введите первое целое число: "))
        operator = input("Введите арифметический знак (+, -, *, /): ")
        num2 = int(input("Введите второе целое число: "))
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Деление на ноль невозможно.")
                return
            result = num1 / num2
        else:
            print("Неверный арифметический знак.")
            return
        print(f"Результат вычисления: {result}")
    except Exception as error:
        print("Введены некорректные данные. Ошибка:", error)
calc()
