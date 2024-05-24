# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в
# первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

from random import randint

n = int(input())
# mas1 = [randint(1, 10) for el in range(n)]
mas1 = [int(el) for el in input().split()]
n2 = int(input())
mas2 = [int(el) for el in input().split()]
# mas2=[randint(1,10) for el in range(n2)]
print(mas1)
print(mas2)

for el in mas1:
    if el not in mas2:
        print(el, end=" ")

