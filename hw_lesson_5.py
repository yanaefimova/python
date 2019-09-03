# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os

# add new list of directories, where name_dir - name directory , count_dir - count of directories
def add_dir(name_dir,count_dir):
	cur_path = os.getcwd()

	list_dir = []

	itm = 1
	while itm <= count_dir:
	  path = f'{cur_path}/{name_dir}_{itm}'
	  os.makedirs(path)
	  itm += 1


# delete list of directories, where name_dir - name directory , count_dir - count of directories
def del_dir(name_dir,count_dir):
	cur_path = os.getcwd()

	list_dir = []

	itm = 1
	while itm <= count_dir:
	  path = f'{cur_path}/{name_dir}_{itm}'
	  os.removedirs(path)
	  itm += 1

# get list of directories
def list_dir():
	cur_path = os.getcwd()
	list_dir = os.listdir(cur_path)

	for itm in list_dir:
		print(itm)

# add_dir("dir",9)
# del_dir("dir",9)

list_dir()

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
