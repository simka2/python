# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве
# серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен
# и нужно вывести номер холодильника, нумерация начинается с единицы.
#
# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие
# латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего
# выводить не нужно.
#
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
#
# Sample Output 1:
# 1 2 3
#
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
#
# Sample Input 3:
# 1
# anton
# Sample Output 3:
# 1
#
# # моё решение
# st_list = [input() for i in range(int(input()))]
# s = 'anton'
# bad_str = []
#
# for i in range(len(st_list)):
#     flag = 0
#     string = st_list[i]
#     cnt = 0
#     for c in s:
#         for j in range(cnt, len(string)):
#             if string[j] == c:
#                 cnt = j + 1
#                 flag += 1
#                 break
#         if flag == 5:
#             bad_str.append(i + 1)
#             break
#
# print(*bad_str)
#
# # от препода через регулярные выражения
# import re
#
# n = int(input())
#
# for i in range(n):
#     s = input()
#
#     if re.search(r"a.*n.*t.*o.*n", s):
#         print(i + 1, end=" ")

# От препода обычное решение
# n = int(input())
# for i in range(n):
#     seq = ["a", "n", "t", "o", "n"]
#     s = list(input())
#     print(f"{s=}")
#     cnt=0
#     while seq and s:  # пока у нас непустые список из букв строки и список слова "anton"
#         cnt+=1
#         if seq[0] == s[0]:  # если буквы равны, то вырываем и там, и там
#             print(f"{seq}          {seq[0]}    {s[0]}")
#             seq.pop(0)
#             s.pop(0)
#         else:  # иначе вырываем только из списка букв строки
#             s.pop(0)
#         print(f"{seq=}       {s=}")
#         print("**"*50)
#     # если список букв слова "anton" пустой, значит вырвали все буквы,
#     # значит в строке встретились все эти буквы в нужном нам порядке
#     print("cnt=", cnt)
#     if not seq:
#         print(i + 1, end=" ")


# чужое решение
# put your python code here
code = ['a', 'n', 't', 'o', 'n']
n = int(input())
infos = [input() for _ in range(n)]


for i in range(n):
    for symbol in code:
        if infos[i].find(symbol) == -1:
            break
        else:
            infos[i] = infos[i][infos[i].find(symbol):]
    else:
        print(i + 1, end=' ')

