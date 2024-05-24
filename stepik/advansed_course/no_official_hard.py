# https://stepik.org/lesson/416755/step/7?thread=solutions&unit=406263
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
#
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 7 4 1
# 8 5 2
# 9 6 3

# моё решение

n = int(input())
mat = [input().split() for _ in range(n)]

mat2 = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(mat[j][i])
    mat2.append(temp)

for i in range(n):
    for j in range(n // 2):
        mat2[i][j], mat2[i][n - 1 - j] = mat2[i][n - 1 - j], mat2[i][j]

for row in mat2:
    print(*row)

# решение препода 1
n = int(input())
matrix = [input().split() for _ in range(n)]
res_matrix = []

for j in range(n):
    cur_column = []  # список для текущего столбца
    for i in range(n):
        cur_column.append(matrix[i][j])

    # полученный столбец мы переворачиваем и запихиваем как ряд в результирующий список
    res_matrix.append(cur_column[::-1])

for row in res_matrix:
    print(*row)


# решение препода 2

n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]
# В первом проходе мы в старой матрице смотрим первый столбец снизу, а записываем его в первую строку с начала
for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)

# решение ученика
n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

for j in range(n):
    for i in range(n):
        print(matrix[n - i - 1][j], end = ' ')
    print()