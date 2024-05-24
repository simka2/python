# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя,
# отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

#
# 1) Добавление контакта:
#  - ввод данных контакта               +++
#  - открыть файл на дозапись (a)       +++
#  - записать в файл                    +++
#
# 2) вывод контактов:
#  - открыть файл на считывание (r)     +++
#  - получить данные из файла           +++
#  - распечатать их                     +++
#
#
# 3) поиск контакта
#  - ввод строки для поиска
#  - открытие файла на чтение (r)
#  - считвывние данных (строки)
#  - поиск контакта
#  - вывод на экран
#
# 4) меню пользователя (юзер интерфейс UI)      +++
#  - создание файла                             +++
#  - вывести на экран меню пользователя         +++
#  - запросить действие у пользователя          +++
#  - выполнение действия                        +++

def input_name():
    return input("Введите имя: ").title()


def input_surname():
    return input("Введите фамилию: ").title()


def input_patronumic():
    return input("Введите отчество: ").title()


def input_phone():
    return input("Введите телефон: ")


def input_address():
    return input("Введите адрес: ").title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronumic} {phone}\n{address}\n\n'


def add_contact():
    """
    Вводим контакт и записываем в файл
    """
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding="UTF-8") as file_a:
        file_a.write(contact)


# 1) Добавление контакта:
#  - ввод данных контакта
#  - открыть файл на дозапись (a)
#  - записать в файл

def print_contacts():
    # with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
    #     print(file_r.read())
    #     print("-" * 50)
    #     print("Вывод контактов завершен")

    with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")


    for i, contact in enumerate(list_contacts, 1):
        print(i, contact)

# def print_contacts():
#     with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
#         print(file_r.read())
#         print("-" * 50)
#         print("Вывод контактов завершен")


# 2) вывод контактов:
#  - открыть файл на считывание (r)
#  - получить данные из файла
#  - распечатать их

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
    search = input("Введите данные для поиска: ")

    with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")

    for contact_str in list_contacts:
        contact_lst = contact_str.split()
        if search in contact_lst[index_var]:
            print("****************")
            print(contact_str)
            print("****************")


# 3) поиск контакта
#  - ввод строки для поиска
#  - открытие файла на чтение (r)
#  - считвывние данных (строки)
#  - поиск контакта
#  - вывод на экран

def interface():
    with open('phonebook.txt', 'a', encoding="UTF-8"):
        pass
    command = ''
    while command != '4':
        print("Варианты действий:\n"
              "1 - ввод контакта\n"
              "2 - вывод контактов\n"
              "3 - поиск контакта\n"
              "4 - выход\n"
              )
        command = input("Введите вариант действия: ")
        while command not in ('1', '2', '3', '4'):
            print()
            print("Введены не корректные данные. Введите число от 1 до 4")
            command = input("Введите вариант действия: ")
        match command:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                print("Всего доброго!")


interface()
