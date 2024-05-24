# https://stepik.org/lesson/416755/step/9?unit=406263
# Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n**2
# (то есть все числа разные) так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между
# собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
# мое решение

def is_mag(cnt):
    for i in range(n):
        if cnt in mat[i]:
            return True
    return False


n = int(input())

mat = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    mat.append(temp)

k = n * 2 + 2
flag = True
cnt = 1

sum_lst = list([0] * (k))
for i in range(n):
    if not flag:
        break
    sum_lst[-2] += mat[i][i]

    sum_lst[-1] += mat[i][n - 1 - i]
    sum_lst[i] = sum(mat[i])

    for j in range(n):
        sum_lst[n + i] += mat[j][i]
        flag = is_mag(cnt)
        cnt += 1

for num in sum_lst:
    if not flag or num != sum_lst[0]:
        print("NO")
        break;
else:
    print("YES")





# от препода
def is_magic_square(n, matrix):
    # создаем список для всех чисел правильной матрицы
    correct_nums = list(range(1, n ** 2 + 1))

    # создаем список для всех чисел нашей матрицы
    our_nums = []
    for row in matrix:
        our_nums.extend(row)

    # если эти списки не равны, значит наша матрица уже не состоит из всех чисел от 1 до n ** 2
    # значит, мы сразу можем вернуть "NO" и не продолжать дальнейшие проверки
    our_nums.sort()
    if our_nums != correct_nums:
        return "NO"

    # в самой матрице мы уже храним все ряды (строки)
    rows = matrix.copy()

    # создаем список для всех столбцов
    columns = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])

        columns.append(cur_column)

    # создаем список для диагоналей (с двумя пустыми подсписками)
    diagonals = [[], []]
    for i in range(n):
        diagonals[0].append(matrix[i][i])
        diagonals[1].append(matrix[i][n - 1 - i])

    # соединям все строки, столбцы и диагонали в один список
    all_lines = rows + columns + diagonals

    # инициализируем переменные для максимальной и минимальной суммы среди всех "линий"
    # за начальные значения возьмём сумму первой "линии"
    max_sum = sum(all_lines[0])
    min_sum = sum(all_lines[0])
    for line in all_lines:
        max_sum = max(max_sum, sum(line))
        min_sum = min(min_sum, sum(line))

    # теперь просто сравниваем максимальную и минимальную суммы
    # они должны быть равны, т.к. все суммы должны быть равны
    if max_sum != min_sum:
        return "NO"

    return "YES"


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

print(is_magic_square(n, matrix))


# от ученика

n = int(input())

mtx = [[int(el) for el in input().split()] for _ in range(n)]

def check_magic_matrix(matrix):
    n = len(matrix)

    #проверка, что все нужные числа представлены
    for num in range(1, n ** 2 + 1):
        if num not in sum(matrix, []):
            return False

    #суммы строк, столбцов и диагоналей
    sum_row_0 = sum(matrix[0])

    ##сравниваем нулевую строку с остальными
    for n_row in range(1, n):
        if sum(matrix[n_row]) != sum_row_0:
            return False
    ##сравниваем нулевую строку с каждым из столбцов
    for n_col in range(n):
        col_total = 0
        for n_row in range(n):
            col_total +=  matrix[n_row][n_col]
        if col_total != sum_row_0:
            return False

    ##сравниваем нулевую строку с диагоналями
    main_diag_total = 0
    other_diag_total = 0
    for n_row in range(n):
        for n_col in range(n):
            if n_col == n_row:
                main_diag_total += matrix[n_row][n_col]
            if n_col + n_row + 1 == n:
                other_diag_total += matrix[n_row][n_col]
    if main_diag_total != sum_row_0 or other_diag_total != sum_row_0:
        return False

    return True

if check_magic_matrix(mtx):
    print('YES')
else:
    print('NO')



# от ученика
# считываем данные
def initial_data():
    # На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
    # затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами
    n = int(input())
    # формирую квадратную матрицу из входных условий
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    return n, matrix


# объявление функции
def magic_square():
    n, matrix = initial_data()
    # print("элементы таблицы matrix =", *matrix, sep="\n")
    # print("элементы таблицы matrix =", matrix)
    # проверяю условие, что все числа в матрице входят в числовую последовательность 1,2,3,…,n ** 2
    # и все числа должны быть разные!!!
    control = [i for i in range(1, n ** 2 + 1)]
    # print("диапазон заданных чисел в матрице =", control)
    s = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in control:
                if matrix[i][j] not in s:
                    s.append(matrix[i][j])
    # print("список уникальных элементов матрицы =", s)
    # print("кол-во элементов в матрице =", n ** 2, "кол-во уникальных элементов в матрице =", len(s))
    if n ** 2 != len(s):
        return "NO"

    row = []
    col = []
    summ_main_diagonal = 0
    summ_side_diagonal = 0
    # вычисляю сумму элементов главной, побочной диагонали и всех строк
    for i in range(n):
        summ_row = 0
        summ_main_diagonal += matrix[i][i]
        summ_side_diagonal += matrix[i][n - i - 1]
        for j in range(n):
            summ_row += matrix[i][j]
        row.append(summ_row)
    # print("summ_main_diagonal =", summ_main_diagonal, "summ_side_diagonal", summ_side_diagonal)
    # print("список сумм элементов всех строк =", row)
    # вычисляю сумму элементов всех столбцов
    for j in range(n):
        summ_col = 0
        for i in range(n):
            summ_col += matrix[i][j]
        col.append(summ_col)
    # print("список сумм элементов всех столбцов =", col)
    target = summ_main_diagonal
    if summ_side_diagonal == target:
        flag = "YES"
    else:
        return "NO"
    for i in range(n):
        if row[i] == col[i] == target:
            flag = "YES"
        else:
            return "NO"

    return flag

    # распаковка матрицы на экран
    # for el in matrix:
    #     print(*el)


# вызываем функцию
print(magic_square())




# от ученика

# put your python code here
n = int(input())
nn = n * n
matrix = [[int(num) for num in input().split()] for _ in range(n)]
sum_r = 0
sum_c = 0
sum_d = 0
sum_dd = 0
chc = []
flag = True

for i in range(n):
    if sum_r == sum_c:
        for j in range(n):
            sum_r += matrix[i][j]
            sum_c += matrix[j][i]
            sum_d += matrix[i][i]
            sum_dd += matrix[i][n - i - 1]
            chc.append(matrix[i][j])
    else:
        break

for i in range(1, nn + 1):
    if i not in chc:
        flag = False
        break

if sum_r == sum_c == sum_d == sum_dd and sum_r == (nn * (nn + 1)) / 2 and flag == True:
    print('YES')
else:
    print('NO')