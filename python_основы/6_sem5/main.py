# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0= 0, a1= 1, ak= ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
cn = 0

# def fib(n):
#     global cn
#     cn += 1
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(8), cn) # тормозит уже на 37 номере. дальше хуже.
# # ---------------
# n1 = 1  # 2
# n2 = 2  # 3
# count = 4
# fib = int(input("Введите число: "))
#
# while n2 < fib:
#     temp = n1  # 2
#     n1 = n2  # 3
#     n2 = temp + n2  # 2+3
#     count += 1
# if n2 > fib:
#     print(n2, count)
# else:
#     print(n2, count)
# ------------------------------------------
#
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# from random import randint
#
# n = int(input("Введите кл-во оценок: "))
#
# list1 = list()
# for i in range(n):
#     list1.append(randint(1, 5))
#
# print(f'Текущие оценки хакера Василия:      {list1}')
#
#
# def search_mx_mn(list1):
#     mx = max(list1)
#     mn = min(list1)
#     return mx, mn
#
#
# max_mark, min_mark = search_mx_mn(list1)
# for i in range(len(list1)):
#     if list1[i] == max_mark:
#         list1[i] = min_mark
#
# print(f'Изменённые оценки хакера Василия:   {list1}')
# -----------------------

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# n = int(input("Введите число: "))
#
#
# def simpl(n):
#     s = 'Число не простое'
#     if n == 1:
#         s = "1 не простое число и не составное."
#         return s
#     if n % 2 == 0 and n != 2:
#         return s
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return s
#     s = "Число простое"
#     return s
#
#
# # Простые числа:
# # 982451653
# # 2000709163
# # 12345678901234969
# print(simpl(n))
# -----------------------------
#
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

from random import randint


# n1 = int(input("ведите число элементов: "))
# s = []
#
#
# def reverse(n):
#     global s
#     if n < 1:
#         return
#     s.append(randint(1, 100))
#     k = s[-1]
#     reverse(n - 1)
#     print(k, end=" ")
#
#
# reverse(n1)
# print()
# print(*s)

# -----------


# def reverse(n):
#     if n < 1:
#         return
#     k = int(input("Введите число: "))
#     reverse(n - 1)
#     print(k, end=" ")
#
#
# num = int(input("Введите количество элементов: "))
# reverse(num)

def reverse(n):
    if n == 1:
        k = input("Введите число: ")
        return k
    k = input("Введите число: ")
    return f'{reverse(n - 1)} {k}'


num = int(input("Введте число элементов: "))
print(reverse(num))
