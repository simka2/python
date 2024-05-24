# На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка
# корректным телефонным номером. Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести «YES», если строка является корректным телефонным номером и «NO» в противном случае.
# Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть
# правильным.
# Sample Input 1:
# 7-301-447-5820
# Sample Output 1:
# YES
# Sample Input 2:
# 301-447-5820
# Sample Output 2:
# YES
# Sample Input 3:
# 301-4477-5820
# Sample Output 3:
# NO

# 1 мое решение

# put your python code here
number = input()
st = "YES"
if not number.replace("-", "").isdigit():
    st = "NO"
else:
    num = number.split("-")
    if (len(num) == 4 and num[0] != '7') or 4 < len(num) or len(num) < 3:
        st = "NO"
    else:
        if len(num) == 4:
            del num[0]
        if len(num[0]) != 3 or len(num[1]) != 3 or len(num[2]) != 4:
            st = "NO"

print(st)

# 2 решение препода

seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")

# 3 от препода (не проходили)
import re

s = input()

if re.fullmatch(r"(7-)?\d{3}-\d{3}-\d{4}", s):
    print("YES")
else:
    print("NO")


# 4 от студента

tel_num = input()
if ((len(tel_num) == 12 and tel_num.count('-') == 2) or
(len(tel_num) == 14 and tel_num[0] == '7' and tel_num.count('-') == 3)):
    if len(tel_num) == 14:
        my_list = tel_num.split('-')
        if (len(str(my_list[1])) == 3) and (len(str(my_list[2])) == 3) and (len(str(my_list[3])) == 4):
            flag = True
            for i in my_list:
                if not(i.isdigit()):
                    print('NO')
                    flag = False
                    break
            if flag:
                print('YES')
        else:
            print('NO')
    else:
        my_list = tel_num.split('-')
        if (len(str(my_list[0])) == 3) and (len(str(my_list[1])) == 3) and (len(str(my_list[2])) == 4):
            flag = True
            for i in my_list:
                if not(i.isdigit()):
                    print('NO')
                    flag = False
                    break
            if flag:
                print('YES')
        else:
            print('NO')
else:
    print('NO')

# 5 от студента
l = input()
if len(l) == 14 and l[:2] == '7-':
    l = l[2:]
if len(l) == 12 and l[3] == '-' and l[7] == '-' and (l[:3] + l[4:7] + l[8:]).isdigit():
    print('YES')
else:
    print('NO')