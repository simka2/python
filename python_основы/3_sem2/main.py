# Задача №9. Общее обсуждение
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input("Введите число: "))
# fac = 1
# i=2
# while i <= n:
#     fac*=i
#     i+=1
# print(fac)
#
# fac = 1
# while n > 1:
#     fac *= n
#     n -= 1
# print(fac)


# ---------------------------

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,

# n1 = 1  # 2
#
# n2 = 2  # 3
# count = 4
#
# fib = int(input("Введите число: "))
#
# while n2 < fib:
#     temp = n1  # 2
#     n1 = n2  # 3
#     n2 = temp + n2  # 2+3
#     count += 1
# if n2 != fib:
#     print(-1)
# else:
#     print(count)


# n1 = 1
# n2 = 2
# count = 4
#
# fib = int(input("Введите число: "))
#
# while n2 < fib:
#     n1, n2 = n2, n1 + n2
#     count += 1
# if n2 != fib:
#     print(-1)
# else:
#     print(count)

# ------------------------

# 2) Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50.
# Нужно вывести наибольшее количество идущих подряд положительных чисел.
#
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

#
# from random import randint  # подклчаем библиотеку и функцию рандома
#
# d = int(input("Сколько будем вводить чисел? "))
# if 1 <= d <= 100:
#     max_pol = 0
#     count = 0
#     for i in range(0, d):
#         temp = randint(-50, 50)
#         print(temp, end=" ")
#         if temp > 0:
#             count += 1
#         else:
#             count = 0
#         if max_pol < count:
#             max_pol = count
# else:
#     print("Число дней должно быть в диапазрне [1,10]")
#
# print("\nМаксимальное число идущих подряд положительных чисел =", max_pol)

# from random import randint
#
# # print(randint(-50, 50))
#
# d = int(input("Введите общее количество дней: "))
# count=0
# max_count=0
# for i in range(d):
#     temp = randint(-50, 50)
#     print(temp, end=" ")
#     if temp>0:
#         count += 1
#         max_count= max(max_count,count)
#     else:
#         count=0
#
# print()
# print(max_count)


# from random import randint
#
# d = int(input("Введите общее количество дней: "))
# count = 0
# max_count = 0
# for _ in range(d):
#     temp = randint(-50, 50)
#     print(temp, end=" ")
#     if temp > 0:
#         count += 1
#     else:
#         max_count = max(max_count, count)
#         count = 0
#
# max_count = max(max_count, count)
# print()
# print(max_count)

# -------------------------------
# Задача №15.  1) Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# 2) Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое.
# Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# from random import randint
#
# kol = int(input("Введите кол-во арбузов: "))
# min_mas = float('inf')
# max_mas = float('-inf')
# for _ in range(kol):
#     mas_arb = randint(1, 20)
#     print(mas_arb, end=" ")
#     max_mas = max(max_mas, mas_arb)
#     min_mas = min(min_mas, mas_arb)
# print(f"Максимальная масса Арбуза = {max_mas=}. Минимальная масса Арбуза = {min_mas=}")

# from random import randint
# N = int(input("Введите количество арбузов: "))
# mass = [randint(1, 100) for _ in range(N)]
# min_mass = max_mass = mass[0]
# print(mass)
#
# for mass in mass:
#     if mass < min_mass:
#         min_mass = mass
#     if mass > max_mass:
#         max_mass = mass
# print("Минимальная масса:", min_mass)
# print("Максимальная масса:", max_mass)


from random import randint

N = int(input("Введите количество арбузов: "))

weights = [randint(1, 100) for _ in range(N)]
min_weight = max_weight = weights[0]

print("Веса арбузов:", weights)

for weight in weights:
    if weight < min_weight:
        min_weight = weight
    if weight > max_weight:
        max_weight = weight

print("Минимальный вес:", min_weight)
print("Максимальный вес:", max_weight)



print('Enter a number:')
n = int(input())
m = 1
while m < n:
    if(m < n):
        if (m * 2 > n):
            break
        else:
            m = m * 2
            print(m)


# print('Enter a number:')
# num = int(input())
# s = 0
# while 2 ** s <= num:
#     print(2 ** s)
#     s += 1