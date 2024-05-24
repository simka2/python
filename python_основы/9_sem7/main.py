# апишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой
# характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то
# False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая
# принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]				same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)

def same_by(func, lst):
    return len(set(map(func, lst))) <= 1


values = [0, 12, 38, 41]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


def same_by2(func, lst):
    asd = list(filter(func, lst))
    return asd == lst or asd == []


if same_by2(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')


def same_by3(characteristic, objects):
    new_list = list(map(characteristic, objects))
    return all(new_list) == any(new_list) or not objects


if same_by3(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')
