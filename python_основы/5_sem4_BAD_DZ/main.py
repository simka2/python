# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже
# встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

#
# text = "a a a b c a a d c d d".split()
#
# dict_text = {}
#
# for el in text:
#     if el not in dict_text:
#         dict_text[el] = 0
#         print(el, end=" ")
#     else:
#         dict_text[el] += 1
#         print(el, dict_text[el], sep="_", end=" ")
#
#
# text="a a a b c a a d c d d".split()
# result_dict={}
# string = ''
# for el in text:
#     if el not in result_dict:
#         string += el + ' '
#     else:
#         string += f'{el}_{result_dict[el]} '
#     result_dict[el]= result_dict.get(el, 0) +1
# string = string.rstrip()


# ------------------
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
#
# Output: 13
#
# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells "
#         "I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea "
#         "shore shells").lower().split()
#
# set_text = set(text)
#
# print(set_text)
# print(len(set_text))
#
#
# unique = []
# count = 0
# for word in text:
#     if word not in unique:
#         unique.append(word)
#         count +=1
#
# print(f'{count = }')
# print(f'{len(unique) = }')
#
# -----------------------------------------------
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
# обратились к Вам, студентам.

# Ваня:
#
# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)
#
# Петя:
#
# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

# Ваня:
# n = int(input())
# max_number = n  # max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number < n:  # max_number > n
#         max_number = n
# print(max_number)

# n = int(input())
# max_number = n # Первая ошибка: max_number = 1000 /Второй вариант: max_number = 0
# while n != 0:
#    n = int(input())
#    if n > max_number: #Вторая ошибка: max_number > n
#        max_number = n
# print(max_number)

# Петя:
#
n = int(input())
max_number = n
while n > 0:   #n < 0
    # n = int(input()) # не на том месте
    if max_number < n:
        max_number =n #  n = max_number
    n = int(input())
print(max_number) #print(n)

