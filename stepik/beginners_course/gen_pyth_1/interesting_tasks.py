# k-ая буква слова
# На вход программе подается натуральное число n и n строк, а затем число  k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе
# нужно игнорировать.
#
# Sample Input:
# 5
# abcdef
# bcdefg
# cdefgh
# defghi
# efghij
# 2
#
# Sample Output:
# bcdef

# put your python code here
# n=int(input())
#
# str_list=[]
# for i in range(n):
#     str_list.append(input())
#
# k=int(input())
#
# for c in str_list:
#     print(c[k-1:k], end="")

# Чужой код
# Иной  взгляд на задачу.  Представьте что вы хотите снизить до минимума время выполнения одного запроса требуемого
# в  условии,  например, вы знаете, что после  считывания данных, вам необходимо будет сделать много таких  запросов
# с разными  значениями позиции k. В таких случаях данные  подвергают предварительной обработке которая называетя
# препроцессинг. В данной задаче  можно сразу формировать список  строк, в котором (k-1) -я строка это  и есть готовый
# ответ на  запрос со значением k! Если в  обычном  решении  для  ответа  потребудется  линейный обход  строк O(n) ,
# то  в данном случая ответ  можно будет  получить за  константное время O(1)  -  время доступа по индексу.
# Обычно  платой за такое быстродействие является время выполнения  препроцессинга и  создание  специальных
# структур данных.  Но  в данном случае,  время  считывания  данных  очевидно пропорционально общему  количеству
# символов на  вводе, ведь  строки всё равно считываются посимвольно! Хотя на первый  взгляд,  мы  видим
# в алгоритме  вложенный цикл, но количество выполняемых действий можно поставить в соответствие  каждому
# считываемому  символу,  такой подход  к подсчёту времени выполонения  алгоритма  называется  амортизационный
# анализ.  На этом основании можно  сделать вывод, что количество операций алгоритма  будет прямо пропорционально
# времени считывания данных с некоторым  коэффициентом!  Количество   строк в  списке может  оказаться  больше
# по сравнению  с оригинальным списком  строк, но  общее  колчиство символов,  а  значить и выделяемый размер
# памяти,  останутся  соизмеримыми, по той же причине.

# КОД
# lst = list()
# for i in range(int(input())):
#     s = input()
#     lst.extend(['']*(len(s) - len(lst)))
#     print(lst)
#     for i, c in enumerate(s):
#         lst[i] += c
# print(lst[int(input())-1])


# @Евгений_Бортников, сразу должен оговориться, что переменная внешнего цикла  i в коде не используется,
# внешний цикл нужен только для повторения действий ровно n раз. Похорошему, вместо  i нужно было поставить
# знак подчёркивания _. Это моё упущение, которое из-за наличая одноименной переменной во вложенном цикле может
# кого-то запутать.  Теперь по поводу алгоритма:
# Итак, lst это список слов - готовых ответов, так что числу  k в запросе соответствует слово с индексом
# k−1 в списке lst (индексация списка идёт с нуля). Проблема в том, что условие задачи никак не ограничивает число
# k, а значит мы заранее не знаем сколько слов выделить в списке lst! Представим как работает алгоритм. Мы считываем
# очередную строку и начинаем добовлять её буквы по порядку в соответствующие слова списка lst. Т.е. например,буква в нулевой позиции строки (первоя буква строки) будет добавлена к слову с индексом 0 в списке lst и т.д. Естественно, мы не можем добавить букву строки, взятую по индексу
# j, в список lst, если в списке lst, на этот момент, еще не создано соответствующее слово под индексом
# j!  Приходим к выводу:
#
# В списке lst должно быть не меньше слов чем букв в  текущей строке!
#
# Но нам известна длина очередной считанной строки, что позволяет нам увеличивать размер списка lst динамически.
# Но строки на вводе могут иметь разную длину! Если очередная строка длиннее предидущих, то размер списка lst придется
# увеличить на len(текущая строка) - len(lst). Но если предидущая строка была длиннее текущей,  то в lst будет
# достаточно слов (просо они уже были добавлены для предидущих строк большей длины). Таким образом команда
#
# lst.extend(['']*(len(s) - len(lst)))
#
# как раз таки и добавляет в список lst недостающие слова и каждое слово инициализировано пустой строкой. В языке
# Python можно создать список определённого размера с помощью оператора *. Его  интересная особенность - только
# умножение на положительное число действительно создает список.
#
# Вместо
#
# for i, c in enumerate(s):
#     lst[i] += c
#
# проще и понятнее было бы написать так:
#
# for i in range(len(s)):
#     lst[i] += s[i]
#
# Тут буквы строки s добовляются в соответствующие слова списка lst. В первом варианте, функция enumerate добавляет перед
# каждым элементом его индекс, на выходе получаются кортежи (индекс, элемент). Чтобы эту пару  вместить,
# в цикле вводятся сразу две переменные i, c.
#
# Если учесть все поправки в коде, то исправленный вариант выглядит так:
#
# lst = list()
# for _ in range(int(input())):
#     s = input()
#     lst.extend(['']*(len(s) - len(lst)))
#     for i in range(len(s)):
#         lst[i] += s[i]
# print(lst[int(input())-1])
