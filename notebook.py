import event as ev
import personal_info as pi

run = True
list_task = {}
personal_data = {}
while run:
    temp_task = input(
        "Введите параметры записи: 1 - добавить событие, 2 - добавить персональные данные,"
        "3 - вывести все записи, 4 - удалить запись, введите 'выход' для выхода из программы\n")

    if temp_task == "1":
        record = ev.Event.add_event(ev.Event)
        current_event = ev.Event(*record)
        if record[0] not in list_task:
            list_value = []
            list_task[record[0]] = list_value
            list_value.append(str(current_event))
        else:
            temp = input("Событие на эту дату уже существует, хотите создать еще одно? Введите 'да' или 'нет'\n")
            if temp == 'да':
                list_value.append(str(current_event))
            elif temp == 'нет':
                print("Cобытие не добавлено")
            else:
                print("Неверный ввод")

    elif temp_task == "2":
        record = pi.PersonalInfo.add_personal_data(pi.PersonalInfo)
        current_data = pi.PersonalInfo(*record)
        if record[0] not in personal_data:
            personal_data[record[0]] = str(current_data)
        else:
            print("Персона уже существует")
    elif temp_task == "3":
        print("__________________")
        print("Журнал событий: ")
        print("__________________")
        for value_temp1 in list_task.values():
            print(value_temp1)
        print("__________________")
        print("Журнал персон: ")
        print("__________________")
        for value_temp2 in personal_data.values():
            print(value_temp2)
    elif temp_task == "4":
        del_temp = input("Какие данные вы хотите удалить? Введите 'событие' или 'персона'\n")
        if del_temp == 'событие':
            temp = input("Введите дату для удаления\n")
            if temp in list_task:
                list_task.pop(temp)
            else:
                print("Неверный ввод")
        elif del_temp == 'персона':
            temp = input("Введите имя для удаления\n")
            if temp in personal_data:
                personal_data.pop(temp)
            else:
                print("Неверный ввод")

    elif temp_task == 'выход':
        print("До встречи")
        run = False
    else:
        print("Не верный ввод!")
