my_set = {12, 234, 45, 5, 678, 456, 45}
text = 'python'
my_list = [11, 22, 33]
num = 999

# my_set.add(text)
# my_set.add(my_list)
# my_set.add(num)

my_set.update(text)
my_set.update(my_list)
my_set.update(num)

# ** ** ** ** ** ** ** ** ** ** ** ** ** *

import copy

# num = 45
# text = 'hello'
my_list = [1, 2, 3, 4, 5, [11, 22, 33, [777, 888, 999]]]
print(my_list)


# my_list_2 = my_list
# print(my_list_2)
# print()
# my_list_2[2] = 999
# print(my_list)
# print(my_list_2)
# print()

def func(new_list):
    new_list[2] = 0


func(my_list)

# my_list_3 = my_list.copy()
# print(my_list_3)
# print()
# my_list_3[3] = 0
# print(my_list)
# print(my_list_3)
# print()

# my_list_4 = my_list[:] # list(my_list)
# print(my_list_4)
# print()
# my_list_4[-1][1] = '~~~~'
# print(my_list)
# print(my_list_4)
# print()

my_list_5 = copy.deepcopy(my_list)
print(my_list_5)
print()
my_list_5[-1][-1][1] = 'XXX'
print(my_list)
print(my_list_5)
# https: // pythontutor.com / render.html  #

import copy

my_tuple = (1, 2, 3, 4, 5, [11, 22, 33, [777, 888, 999]])
print(my_tuple)

# my_tuple_2 = my_tuple[:]
# print(my_tuple_2)
# print()
# my_tuple_2[-1][1] = '~~~~'
# print(my_tuple)
# print(my_tuple_2)
# print()

my_tuple_3 = copy.deepcopy(my_tuple)
print(my_tuple_3)
print()
my_tuple_3[-1][-1][1] = 'XXX'
print(my_tuple)
print(my_tuple_3)


# --------------

my_dict = {'Иванов': 1, 'Петров': 2, 'Сидоров': 3, 'Николаев': 4}
# print(f'{my_dict=}')
# print(f'{my_dict["Петров"]=}')
# print()
print(my_dict)
print(my_dict["Петров"])
print()
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print()
# print(f'{len(my_dict.keys())=}')
# print(f'{sum(my_dict.values())=}')
# print(f'{my_dict.items()=}')
# print()
# print(f'{list(my_dict.keys())[3]=}')
# print(f'{list(my_dict.values())=}')
# print(f'{list(my_dict.items())=}')
# print()

# for key in my_dict:
#     print(key, end='\t')
# print('\n')

# for key in my_dict.keys():
#     print(key, end='\t')
# print('\n')

# for value in my_dict.values():
#     print(value, end='\t')
# print('\n')

# for item in my_dict.items():
#     print(item, end='\t')
# print('\n')

for key, value in my_dict.items():
    print(key, value, sep='-', end='\t')
print('\n')

# q,w,*e = (111,222,333)
# print(q)
# print(w)
# print(e)

my_list = [(1, 2), (11, 22, 33, 44), (111, 222, 333)]
for q, w, *e in my_list:
    print(q, w, e, sep='-')

for key, value in my_dict.items():
    print(key, value, sep=': ', end='\t')
print('\n')

my_dict = {'Иванов': 1, 'Петров': 2, 'Сидоров': 3, 'Николаев': 4}

text = 'hello world!'
text = text[6:] + ' ' + text[: 5]

# my_dict['Алексеев'] = my_dict['Петров']
# del my_dict['Петров']

my_dict['Алексеев'] = my_dict.pop('Петров')

from random import randint

nums_list = [randint(1, 5) for _ in range(5)]

nums_set = {randint(1, 5) for _ in range(5)}

nums_dict = {i: randint(1, 5) for i in range(5)}

nums_gen = (randint(1, 5) for _ in range(5))