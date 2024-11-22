def calculate_structure_sum(data):
    summ = 0
    ss=0
    for el in data:
        #print(f" -----{type(el)}---------{el}")
        if isinstance(el, list):
            ss = (calculate_structure_sum(el))                  # Рекурсивный вызов для вложенного списка
            summ +=ss
            #print(f" list {el} calculate_structure_sum(el)={ss} summ = {summ}")
        elif isinstance(el, dict):
            summ += calculate_structure_sum(el.keys())          # Рекурсивный вызов для вложенного словаря
            summ += calculate_structure_sum(el.values())
            #print(f" dict {el} calculate_structure_sum(el)={ss} summ = {summ}")
        elif isinstance(el, tuple):
            summ += calculate_structure_sum(el)                  # Рекурсивный вызов для вложенного картежа
            #print(f" tuple {el} calculate_structure_sum(el)={ss} summ = {summ}")
        elif isinstance(el, str):
            summ += len(el)
            #print(f" str {el} calculate_structure_sum(el)={ss} summ = {summ}")
        else:
            summ += el
    return summ

data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [(2, 'Urban', ('Urban2', 35))]) ]
#data_structure = [1, [2, 3], "Hello", {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8})]
result = calculate_structure_sum(data_structure)
print(result)

