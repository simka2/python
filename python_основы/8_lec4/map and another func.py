# #map(x, y)  # применяет к y функцию x
lst = [x for x in range(20)]
lst = list(map(lambda x: x + 10, lst))
print(lst)

# filter(x, y) - возвращает y, если он удовлетворяет условию x
a = [1, 2, 3, 5, 8.45, 15, 23, 38]
res = list(filter(lambda x: x % 2 == 0, a))
print(res)

# zip(a,b, ...) - из списков a,b,c создает кортежи, где в каждом кортеже будут члены с одинаковым индекосом.
# Работает по минимальному списку.

a = ['users1', 'users2', 'usrrs3', 'users4']
b = [1, 25, 23, 49]
c = ['coffe', 'eda', 'sok']
res = list(zip(a, b, c))  # [('users1', 1, 'coffe'), ('users2', 25, 'eda'), ('usrrs3', 23, 'sok')]
print(res)

a = ['users1', 'users2', 'usrrs3', 'users4']
asd = list(enumerate(a))  # применяется к итерируемому объекту и возвращает новый итератор с кортежами и з индекса и
# элементов входных данных  #[(0, 'users1'), (1, 'users2'), (2, 'usrrs3'), (3, 'users4')]
print(asd)


# a = [1, 2, 3, 5, 8, 15, 23, 38]
#
# lst = []
# for num in a:
#     if num % 2 == 0:
#         temp = (num, num ** 2)
#         lst.append(temp)
# print(lst)


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if (f(x))]


a = [1, 2, 3, 5, 8.45, 15, 23, 38]
print(f'{a=}')
res = map(int, a)

res = filter(lambda x: x % 2 == 0, res)

res = list(map(lambda x: (x, x ** 2), res))

print("_" * 50)

lst = [x for x in range(20)]
lst = list(map(lambda x: x + 10, lst))
print(lst)




# all and any
print(all([True, True, True, True]))
print(all([True, False, True, True]))
print(all([False, False, False, False]))
print()
print(any([True, True, True, True]))
print(any([True, False, True, True]))
print(any([False, False, False, False]))
print()
print(all([1, 2, 3, 4]))
print(all([1, 0, 3, 4]))
print(all([0, 0, 0, 0]))
print()
print(any([1, 2, 3, 4]))
print(any([1, 0, 3, 4]))
print(any([0, 0, 0, 0]))
print()
print(all(['dfg', 'sdf', 'sdf', 'cvb']))
print(all(['dfg', '', 'sdf', 'cvb']))
print(all(['', '', '', '']))
print()
print(any(['dfg', 'sdf', 'sdf', 'cvb']))
print(any(['dfg', '', 'sdf', 'cvb']))
print(any(['', '', '', '']))
print()
print(all([[''], ('',), {''}, ['']]))
print(all([[''], [], [''], ['']]))
print(all([{}, {}, {}, []]))
print()
print(any([[''], ('',), {''}, ['']]))
print(any([[''], [], [''], ['']]))
print(any([{}, {}, {}, []]))
print()
