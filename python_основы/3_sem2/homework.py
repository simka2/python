# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы
# все монетки лежали одной и той же стороной вверх.
#
# Входные данные:
#
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1,
# если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
#
# Выходные данные:
#
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
#
#
# Пример использования На входе:
# coins = [0, 1, 0, 1, 1, 0]
# На выходе:
# 3


# coins = [0, 0, 0, 0, 1, 1]
# eagle = 0
# tails = 0
#
# for i in coins:
#     if i == 1:
#         eagle += 1
#     else:
#         tails += 1
# if eagle > tails:
#     print(tails)
# else:
#     print(eagle)
#
# ------------------------------------------

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны
# вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
#
# На входе:
# s = 12
# p = 27
# На выходе:
# 3 9

# x+y=12
# x*y=27
# x=12-y
#
# (12-y)*y=27
# 12y-y2=27
# y2-12y+27=0
# D=b2-4ac)=(12*12-4*1*27)=(144-108)=36
# x1=(-b-sqr(d))/2a=(12-6)/2=3
# x2=x1=(-b+sqr(d))/2a=(12+6)/2=9
#
# y1=12-x=12-3=9
# y2=12-9=3
#

# s = 12
# p = 27
# d = (-s) ** 2 - 4 * p
# x1 = int((s - (d ** 0.5)) / 2)
# y1 = s - x1
#
# x2 = int((s + (d ** 0.5)) / 2)
# y2 = s - x2
#
# if x1 > y1:
#     print(x2, y2)
# else:
#     print(x1, y1)

# s = 12
# p = 27
# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))
#
# for solution in solutions:
#     print(solution[0], solution[1])


# -------------------------
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
#
# Пример
# n=16
# #Вывод
# 1
# 2
# 4
# 8
# 16

# n=16
# for i in range(0,n):
#     a=2**i
#     if (a>n):
#         break
#     print(a)
#
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

a=3**2**5
print(a)
