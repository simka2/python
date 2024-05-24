# Дан список чисел. Определите, сколько в нем встречается различных чисел.
#
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
#
# Output: 6

# from random import randint
#
# size = int(input("Введите размер массива: "))
# list_1 = []
#
# for _ in range(size):
#     list_1.append(randint(-10, 10))
#
# # print(list_1)
#
#
# list_1 = [randint(1, 100) for _ in range(size)]
#
# print(list_1)

# # Решение Евгения Исакова (ученик)
# unic = []
# for temp in list_1:
#     if (temp in unic):
#         continue
#     else:
#         unic.append(temp)
# print(unic)
# print(len(unic))


# Решение от преподавателя 1:

# print(len(set(list_1)))

# Решение от преподавателя 2:

# uniq = []
# count = 0
# for el in list_1:
#     if el not in uniq:
#         uniq.append(el)
#         count += 1
# print(count)

# ---------------------------------
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан изначально.
#
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# k = int(input("Ввежите сдвиг: ")) % len(my_list)
# #
# print(my_list[-k:] + my_list[:-k])
# #
# # # Решение Евгения Исакова (ученик)
# # for i in range(k):
# #     my_list.insert(0, my_list[len(my_list) - 1])
# #     my_list.pop()
# #
# # print(my_list)
#
# # Решение от преподавателя №2
# for _ in range(k):
#     # last = my_list.pop()
#     # my_list.insert(0, last)
#     # или
#     my_list.insert(0, my_list.pop())
# print(my_list)
#

# -------------------------------
# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
#               {"VIII": "S007"}]
#
# my_dict = set()
# my_dict2 = set()
# my_dict3 = set()
# my_dict3b = set()
#
# list_dicts = [{"V": "S001", "ty": "s0001212"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#               {"V": "S009"},
#               {"VIII": "S007"}]
# for current in list_dicts:
#     for k in current:
#         my_dict.add(current[k])
#
# # решение 2
# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
#               {"VIII": "S007"}]
# for current in list_dicts:
#     my_dict2.add(*current.values())
#
# # решение 3
# list_dicts = [{"V": "S001", "ty": "s0001212"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#               {"V": "S009"},
#               {"VIII": "S007"}]
# for current in list_dicts:
#     my_dict3.update(current.values())
#
# # решение 3 c ошибкой
# list_dicts = [{"V": "S001", "ty": "s0001212"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#               {"V": "S009"},
#               {"VIII": "S007"}]
# for current in list_dicts:
#     my_dict3b.update(*current.values())
#
# print(my_dict)
# print(my_dict2)
# print(my_dict3)
# print(my_dict3b)

# --------------------------

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

# my_list=[0, -1, 5, 2, 3]
# from random import randint
#
# k=int(input("Введите размер массива: "))
#
# my_list=[randint(-5,5) for _ in range(k)]
# print(my_list)
#
# cnt=0
# for i in range(len(my_list)-1):
#     if my_list[i]<my_list[i+1]:
#         cnt+=1
# print(cnt)


# -----------------------------------
# дз
# задача 3
# функция:
# def isEnglish(letter): # состоит ли строка из английских букв
# return letter.isascii() and letter.isalpha()
# if letter.isascii() and letter.isalpha():
# print('строка состоит из английских букв')
