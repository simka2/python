# https://stepik.org/lesson/416755/step/8?thread=solutions&unit=406263
# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые
# бьёт конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь, отметьте символами *,
# остальные клетки заполните точками.
#
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4, где сначала
# записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).
#
# Sample Input 1:
# b6
# Sample Output 1:
# * . * . . . . .
# . . . * . . . .
# . N . . . . . .
# . . . * . . . .
# * . * . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .

# Мое решение
def pole():
    mat = [["."] * 8 for _ in range(8)]
    return mat


def knight(row, col):
    mat = pole()
    mat[row][col] = 'N'
    if row + 2 < 8 and col + 1 < 8:
        mat[row + 2][col + 1] = '*'
    if row + 2 < 8 and col - 1 >= 0:
        mat[row + 2][col - 1] = '*'
    if row - 2 >= 0 and col + 1 < 8:
        mat[row - 2][col + 1] = '*'
    if row - 2 >= 0 and col - 1 >= 0:
        mat[row - 2][col - 1] = '*'

    if row + 1 < 8 and col + 2 < 8:
        mat[row + 1][col + 2] = '*'
    if row + 1 < 8 and col - 2 >= 0:
        mat[row + 1][col - 2] = '*'
    if row - 1 >= 0 and col + 2 < 8:
        mat[row - 1][col + 2] = '*'
    if row - 1 >= 0 and col - 2 >= 0:
        mat[row - 1][col - 2] = '*'
    return mat


col, row = list(input())
alf = 'abcdefgh'
col = alf.index(col)
row = 8 - int(row)

mat = knight(row, col)
for n in mat:
    print(*n)

# от препода
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)

# от препода
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'

for row in board:
    print(*row)

# от ученика
xy = input()
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

column = columns.index(xy[0])
row = 8 - int(xy[1])

matrix = [['.' for _ in range(8)] for _ in range(8)]
matrix[row][column] = 'N'

for i in range(8):
    for j in range(8):

        if abs(row - i) * abs(column - j) == 2:
            matrix[i][j] = '*'

        elif (row - 2 > i or row + 2 < i) or (column + 2 < j):
            break

    print(*matrix[i])


# от ученика, со словарями
# функция для определения, находятся ли координаты позиций внутри шахматного поля

def is_position_in_desk(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False

# словарь со значениями клеток шахматной доски
chess_desk = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
# считывание шахматной позиции и перевод в координаты
position = input()
row_pos = chess_desk[int(position[1])]
col_pos = chess_desk[position[0]]
# создание матрицы 8*8, обозначение позиции коня
result_desk = [['.'] * 8 for _ in range(8)]
result_desk[row_pos][col_pos] = 'N'
# i принимает только значения -1 и 1, а j принимает только значения -2 и 2
for i in range(-1, 2, 2):
    for j in range(-2, 3, 4):
        if is_position_in_desk(row_pos + i, col_pos + j):
            result_desk[row_pos + i][col_pos + j] = '*'
        if is_position_in_desk(row_pos + j, col_pos + i):
            result_desk[row_pos + j][col_pos + i] = '*'
# выводим получившуюся матрицу
for r in range(8):
    for c in range(8):
        print(result_desk[r][c], end=' ')
    print()


# от ученика
# считываем данные
def initial_data():
    # На вход программе подаются координаты коня на шахматной доске в шахматной нотации
    # (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо),
    # затем номеру строки (цифра от 1 до 8, снизу вверх)).
    point = input()
    coordinates = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['8', '7', '6', '5', '4', '3', '2', '1']]
    # перевожу шахматные координаты в индексы i, j
    x, y = coordinates[1].index(point[1]), coordinates[0].index(point[0])
    # print("x =", x, "y =", y)
    # формирую матрицу шахматного поля c нулями
    # т.к. не надо будет производить математических операций над элементами матрицы,
    # то числа можно оставить в строковом формате
    matrix = [["."] * 8 for _ in range(8)]
    matrix[x][y] = "N"
    return x, y, matrix


# объявление функции
def knight_moves():
    x, y, matrix = initial_data()
    # print("элементы таблицы matrix =", *matrix, sep="\n")
    # print("элементы таблицы matrix =", matrix)
    for i in range(8):
        for j in range(8):
            if abs(x - i) == 1 and abs(y - j) == 2:
                matrix[i][j] = "*"
            elif abs(x - i) == 2 and abs(y - j) == 1:
                matrix[i][j] = "*"


    # распаковка матрицы на экран
    for el in matrix:
        print(*el)

    return ""


# вызываем функцию
print(knight_moves())