from logger import *


def interface():
    with open('phonebook.txt', 'a', encoding="UTF-8"):
        pass
    command = ''
    while command != '6':
        print("Варианты действий:\n"
              "1 - ввод контакта\n"
              "2 - вывод контактов\n"
              "3 - поиск контакта\n"
              "4 - удаление контакта\n"
              "5 - копирование контакта в другой файл\n"
              "6 - выход\n"
              )
        command = input("Введите вариант действия: ")
        while command not in ('1', '2', '3', '4', '5', '6'):
            print()
            print("Введены не корректные данные. Введите число от 1 до 6")
            command = input("Введите вариант действия: ")
        match command:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                del_contact()
            case '5':
                copy_contact()
            case '6':
                print("Всего доброго!")



