def send_email(massage,recipient,sender="university.help@gmail.com"):
    for el in sender:
        if el == "@":
            res = True
            break
        else:
            res = False
    if res == False:
        return "1Невозможно отправить письмо с адреса", sender,"на адрес", recipient
    for el in recipient:
        if el == "@":
            res =True
            break
        else:
            res = False
    if res== False:
        return "2Невозможно отправить письмо с адреса", sender,"на адрес", recipient
    if (sender.endswith(".net") or sender.endswith(".com") or sender.endswith(".ru")) and (recipient.endswith(".net") or recipient.endswith(".com") or recipient.endswith(".ru")):
        if recipient == sender:
            return "Нельзя отправить письмо самому себе!","","",""
        if sender != "university.help@gmail.com":
            return "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса",sender,"на адрес", recipient
        return "Письмо успешно отправлено с адреса", sender, "на адрес", recipient
    else:
        return "3Невозможно отправить письмо с адреса", sender,"на адрес",  recipient

otvet1,otvet2,otvet3,otvet4 = send_email('Просто положительная проверка',"develor@mail.ru")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка отсутствия @ у отправителя',"volvo@mail.ru","universitymail.com")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка отсутствия @ у получателятеля',"volvomail.ru")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка домена у отправителя',"domen@mail.ru","university@mail.c")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка домена у получателятеля',"domen@mail.dom")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка отправки самому себе',"university.help@gmail.com")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")
otvet1,otvet2,otvet3,otvet4 = send_email('Проверка нестандартного отправителя',"kinder@mail.ru", "notstandart@mail.com")
print(f"{otvet1} {otvet2} {otvet3} {otvet4}")


