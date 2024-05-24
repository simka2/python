from date_create import *

file_bd_name = 'phonebook.txt'


def add_contact():
    """
    Вводим контакт и записываем в файл
    """
    contact = create_contact()
    with open(file_bd_name, 'a', encoding="UTF-8") as file_a:
        file_a.write(contact)


def print_contacts():
    with open(file_bd_name, 'r', encoding="UTF-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")

    print('id   Контакт')
    print("-" * 40)
    for i, contact in enumerate(list_contacts, 1):
        print(str(i).ljust(4), contact)
    print("-" * 40)


def search_contact():
    print("Варианты поиска:\n"
          "1 - по Фамилии\n"
          "2 - по имени\n"
          "3 - по отчеству\n"
          "4 - по телефону\n"
          "5 - по адресу\n"
          )
    var = input("Введите вариант поиска: ")
    while var not in ('1', '2', '3', '4', '5'):
        print()
        print("Введены не корректные данные. Введите число от 1 до 5")
        var = input("Введите вариант поиска: ")
    index_var = int(var) - 1
    search = input("Введите данные для поиска (регистронезависимые): ").lower()

    with open(file_bd_name, 'r', encoding="UTF-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")

    for contact_str in list_contacts:
        contact_lst = contact_str.split()
        if search in contact_lst[index_var].lower():
            print("_" * 20)
            print(contact_str)
    print("-" * 20)


def del_contact():
    with open(file_bd_name, 'r', encoding='UTF-8') as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")
    list_contacts = list(enumerate(list_contacts, 1))
    len_contacts = len(list_contacts)

    if len_contacts == 1 and list_contacts[0][1] == '':
        print("Файл пустой! Удалять нечего!")
        return
    id_contact_del = input("Введите номер id для удаления: ")
    while not (id_contact_del.isdigit() and 1 <= int(id_contact_del) <= len_contacts):
        print("Введен не id или такого id не существует")  # если у нас пустой файл, будут проблемки... :-)
        id_contact_del = input("Введите номер id для удаления: ")
    id_contact_del = int(id_contact_del)

    with open(file_bd_name, 'w', encoding='UTF-8') as file_w:
        for i in range(len(list_contacts)):
            if i + 1 == id_contact_del:
                continue
            copy_str = list_contacts[i][1] + "\n\n"
            file_w.write(copy_str)
    print(f"Удаление контакта с id = {id_contact_del} успешно завершено!")


def copy_contact():
    with open(file_bd_name, 'r', encoding='UTF-8') as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")
    list_contacts = list(enumerate(list_contacts, 1))

    print("Варианты ввода:\n"
          "'id' - номер строки, которую будем копировать\n"
          "0    - копируем весь файл\n"
          "-1   - отмена копирования\n"
          )

    copy_id = input("Введите id: ")
    if copy_id == '-1':
        return
    while not (copy_id.isdigit() and (-1 <= int(copy_id) <= len(list_contacts))):
        print()
        print("Введены не корректные данные. Введите 'номер id' или '0' или '-1'")
        copy_id = input("Введите id: ")
        if copy_id == '-1':
            return
    copy_id = int(copy_id)

    copy_name_file = input("Введите полное название файла, в который будем копировать: ")
    while copy_name_file == file_bd_name:
        print("введите другое имя файла для копирования. Введенное имя занято основной базой данных.")
        copy_name_file = input("Введите полное название файла, в который будем копировать: ")

    with open(copy_name_file, 'a', encoding="UTF-8") as file_a:
        if copy_id != 0:
            copy_str = list_contacts[copy_id - 1][1] + "\n\n"
            file_a.write(copy_str)
        else:
            for i in range(len(list_contacts)):
                copy_str = list_contacts[i][1] + "\n\n"
                file_a.write(copy_str)
    print("Копирование успешно завершено!")
    print("-" * 35)
