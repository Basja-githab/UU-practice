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
#calc()
print(range(3))
dict = {}
dict["name"] = 'bhf'
dict.pop("name")
print(dict)
#python
my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))
my_set = {1,2,3}
my_set.add(4)
print(my_set)
def my_function(x):
    return x + 1
print(my_function(5))