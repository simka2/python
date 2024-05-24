# Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик
# Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было
# 1729, такое скучное и заурядное число. На что Рамануджан ответил:
# Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух
# кубов двумя разными способами. Другими словами:
# 1729 =1**3 + 12**3=9**3+10*3
#
# Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые
# 5 чисел в порядке возрастания, включая число 1729

cnt = 0
for n1 in range(1, 70):

    for n2 in range(1, 70):
        for n3 in range(1, 70):
            if n3 == n1 or n3 == n2:
                continue
            for n4 in range(1, 70):
                if n4 == n1 or n4 == n2:
                    continue
                if (
                        n1 ** 3 + n2 ** 3 == n3 ** 3 + n4 ** 3) and n1 != n4 and n2 != n3 and n2 != n4 and n1 > n2 and n1 > n4 and n1 > n3:
                    print(f'{n1}**3 + {n2}**3 = {n3}**3 + {n4}**3 = {n1 ** 3 + n2 ** 3}')
                    cnt += 1
                if cnt == 50:
                    break
            if cnt == 50:
                break
        if cnt == 50:
            break
    if cnt == 50:
        break

# Ни одного нормального решения с пояснениями я тут не нашел. Поэтому настало время для удивительных историй.
# Уравнение a^3 + b^3 = c^3 + d^3 = x
# 1. Все числа в этом неравенстве должны быть разные. Об этом не сказано прямым текстом в задаче, но это должно быть
# понятно чисто логически. Если предположим a = b, то и с правой части c = d, да еще и между собой они тоже получается
# должны быть равны, т.е. a = b = c =d. Тогда вся эта задача не имеет никакого смысла. Также 'a' не может равняться 'c'
# или 'd', т.к. в этом случае другая пара тоже должна быть равна между собой. Т.е. если например a = c, то и b
# должно быть = d. Или если a = d, то и b должно быть = c. Попробуйте написать на листочке, подставив реальные числа.

# 2. Граница перебора. Для того, чтобы программа вывела только 5 чисел, нам необходимо или указать случайно на глаз
# границу перебора для искомых a, b, c, d или поставить счетчик принтов, чтобы после 5 принта операция прерывалась.
# Границы перебора я заметил тут ставят кто какие, видел и 33 и 50 и 100 и 5000 и т.д. у кого насколько фантазии.
# Опытыным путем можно установить, что чтобы программа нам нашла только 5 решений уравнения, все числа должны быть
# не более 33. Если какое то из чисел больше 33, то у программы больше вариантов и она найдет больше решений.
# Чем больше диапазон для чисел, тем больше решений выдаст программа.

# 3. В первом пункте мы установили, что все числа должны быть разные, иначе уравнение будет решаться типа
# 1 + 8 = 8 +1 или 9 + 9 = 9 + 9 и тогда даже если числа будут не более 33, то программа нам найдет еще 100500 решений.
# Если все числа разные, то логично предположить, что между ними есть какая то закономерность по возрастанию.
# Разберем на примере.
# 1^3+12^3 = 9^3+10^3, т.е. интервал с одной стороны равенства включает в себя числа интревала с другой стороны равенства
# [1_________ [9 _10] __12], т.е. если числа оба числа слева не могут быть одновременно больше или одновременно
# меньше обоих числе справа.
# Соотвественно мы можем описать закономерность в которой [a < [c < d] < b] или наоборот [c < [a < b] < d].
# Т.е. просто распологаем быквы в порядке возрастания, так чтобы числа с одной равенства были внешними границами,
# а числа с другой стороны неравенства были внутренними границами.
# Итак [a > c > d > b.

# 4. Теперь финиш, нам надо перенести это всё в питончик. У нас есть 4 неизвестных, т.е. нам необходимы 4 цикла,
# чтобы на каждом из циклов перебиралась оодна из незивестных. Самая удобно воспринимаемая аналогия, это кодовый замок
# на котором мы поочередно вращаем колесики.
# Помимо 4 циклов нам разумеется надо записать и само уравнение a^3 + b^3 = c^3 + d^3.
# И тут ты мой мозговитый друг справедливо заметишь, а как же тот факт, что все эти числа не равны. Отвечаю.
# Писать об этом прямым текстом в программу нет смысла. Факт того что все переменные между собой не равны
# и что в них есть закономерность по возрастанию мы отразим задавая границы циклов
# (тем самым мы еще и количество циклов уменьшим, сократив тем самым время выполнения программы).
# Напомню, мы условно приняли, что  a > c > d > b. Значит создаем цикл для перебора 'a', потом для перебора 'с',
# потом 'd' и в конце 'b'. Первоначально границу цикла можно взять любую, но опытным упем люди до нас уже установили,
# что 5 решений будет если она не выше 33. Поэтому условно берем 33. Переменная 'a' у нас самая большая,
# поэтмоу ей и дается самый большой диапазон. Переменная 'с' у нас не больше чем 'a', поэтому ограничиваем её
# диапазон от 1 до 'a'. С остальными аналогично. Получается, что все переменные по своиему значению у нас никогда
# между собой не пересекуться. И у нас у программе не будет лишних циклов.

# 5. Вопрос с расположением чисел в порядке возрастания. Т.к. мы расположили циклах поиска переменных в порядке
# возрастания и т.к. программа начинает искать возможные значения переменных с 1, то она априори найдет сначала
# наименьшие из возможных значений переменных, а значит даст первоначально наименьший результата уравнения.
# И будет искать дальше в порядке возрастания.

print("-"*20)
for a in range(1, 33):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a ** 3 + b ** 3)
print("-"*20)
arr3 = [i ** 3 for i in range(1, 33)]  # Создаем список со всеми кубами
summ_cube = [a + b for a in arr3 for b in arr3 if a > b]  # Создаем список с суммами кубов
ram = set(i for i in summ_cube if summ_cube.count(i) == 2)  # Множество сумм, встречающихся ровно 2 раза
ram_li = sorted([i for i in ram])  # Сортируем
print(ram_li)

print("-"*20)
import itertools
n = 33
l = [x[0] ** 3 + x[1] ** 3 for x in itertools.combinations(range(1, n), 2)]
visit = set()
n_rama = [el for el in l if el in visit or visit.add(el)]
print(sorted(n_rama))