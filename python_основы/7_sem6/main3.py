# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3	2 2		2

lst = [int(el) for el in input().split()]

size = len(lst)
counter = 0
for i in range(size - 1):
    for j in range(i + 1, size):
        if lst[i] == lst[j]:
            counter += 1
print("Число дубликатов", counter)

counter=0
for i in range(size - 1):
    # print(f'{lst[i + 1:]=}   {lst[i]=}', lst[i + 1:].count(lst[i]))
    counter += lst[i + 1:].count(lst[i])
print("Число дубликатов_2 вариант", counter)
