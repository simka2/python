# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике
# на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#
# На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника Паскаля
# в виде списка (нумерация строк начинается с нуля).
#
# Формат входных данных
# На вход программе подается число n(n≥0)
#
# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.

# мое решение

def pascal(n):
    lst = [[1]]
    if n == 0:
        return lst
    for i in range(1, n + 1):
        el = [0 for _ in range(0, i + 1)]
        a = len(el)
        for j in range(a):
            if j == 0 or j == a - 1:
                el[j] = 1
            else:
                el[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(el)
    return [el]


n = int(input())
print(*pascal(n))


def pascal2(n):
    lst = [[1]]
    if n == 0:
        return lst

    for i in range(1, n + 1):
        tmp1, tmp2 = lst[i - 1].copy(), lst[i - 1].copy()
        tmp1.append(0)
        tmp2.insert(0, 0)
        el = []
        for i in range(len(tmp1)):
            el.append(tmp1[i] + tmp2[i])
        lst.append(el)
    return [el]


print(*pascal2(n))


def pascal3(n):
    # начальная строка
    cur_seq = [1]

    for _ in range(n):
        # добавляем нули по бокам к текущей строке строке
        cur_seq = [0] + cur_seq + [0]
        # тут будет храниться новая строка
        new_seq = []

        for i in range(len(cur_seq) - 1):
            # добавляем в новую строку сумму соседних элементов текущей строки
            new_seq.append(cur_seq[i] + cur_seq[i + 1])

        # теперь новая строка становится нашей текущей строкой
        cur_seq = new_seq

    return cur_seq


print(pascal3(n))


def pascal4(n):
    list = [[1]]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1:
                list.append([1])
            elif i != 1 and j != 1:
                list[i].extend([list[i - 1][j - 1] + list[i - 1][j - 2]])
            if j == i:
                list[i].extend([1])
    print(list[n])


pascal4(n)
