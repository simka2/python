# режимы открытия файлов:
#
# a # открытие для добавления данных. Если файла нет, то он будет создан.
# # Если файл есть, то данные будут добавляться к имеющимся
#
# r # открытие для чтения данных. Если файла нет, будет ошибка
#
# w # открытие для записи. Если файла нет, будет создан. Если есть, то данные будут перезаписываться.
#
# w+ # открытие для записи и чтения. Если файла нет, будет создан.
#
# r+  # открытие для чтения и дописывания в файл. если файла нет, то будет ошибка.


colors = ['red', 'Петя', 'blue']
data = open('my_file.txt', 'a', encoding='utf-8')
data.writelines(colors)
data.close()

# colors = ['red', 'Петя', 'blue']
# data = open('my_file.txt', 'a', encoding='utf-8')
# data.write('\n\nПетя ушел гулять')
# data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# with open('file.txt', 'w') as data:
#     data.writelines("asd")

path = 'file.txt'
path2 = 'my_file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# МОДУЛЬ OS
# функции для работы с операционной системой.
import os
path="E:/учеба/5 python основы"
os.chdir(path) # смена текущей директории

a = os.getcwd()  # текущая рабочая директория
print(a)

# os.path # вложенный модуль в модуль os.
#
# os.path.basename(path) # базовое имя пути
#
# os.path.abspath(path) # возвращает нормализованный абсолютный путь


# модуль shutil
import shutil
# содержит функци для обработки файлов, групп файлов и папок. К примеру копировать, перемещать и удалять

shutil.copyfile(src, dst) # копирует содержимое (но не метаданные) файла src в файл dst

shutil.copy(src, dst) # копирует содержимое файла src в файл или паку dst

# path='e:/temp/asdf3443434343434'
# shutil.rmtree(path) # удаляет текущую директорию и все поддиректории; path должен указывать на
# # директорию, а не на символическую ссылку