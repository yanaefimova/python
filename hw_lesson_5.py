# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import re
import shutil

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

# add new directory
def add_one_dir(name_dir):
    cur_path = os.getcwd()
    path = f'{cur_path}/{name_dir}'
    os.makedirs(path)
    print("Add :", path)

# delete selected directory
def del_one_dir(name_dir):
    cur_path = os.getcwd()
    path = f'{cur_path}/{name_dir}'
    os.removedirs(path)
    print("Delete :", path)

# show list of directories
def list_dir():
    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)

    for itm in list_dir:
        print(itm)

# copy file
def copy_file():
    cur_path = os.getcwd()
    cur_file = os.path.realpath(__file__)

    pat = r'[^/][0-9a-zA-z]+'
    file_name = re.findall(pat,cur_file)[-2]
    file_format = re.findall(pat,cur_file)[-1]
    copy_file = f'{cur_path}/{file_name}_copy{file_format}'
        
    if os.path.isfile(copy_file) != True:
        shutil.copy(cur_file, copy_file)
        mess = f'file copy created : {copy_file}'
    else:
        mess = f'file copy is exists : {copy_file}'

    return mess

# open selected directory
def open_dir(name_dir):
    cur_path = os.getcwd()
    path = f'{cur_path}/{name_dir}'
    os.chdir(str(path))
    print("Open :",path)

# add_dir("dir",9)
# del_dir("dir",9)
# list_dir()
# print(copy_file())
# open_dir("dir_1")


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

from test import open_dir, list_dir, del_one_dir, add_one_dir

command_menu = {1:"Перейти в папку", 2:"Просмотреть содержимое текущей папки", 3:"Удалить папку", 4:"Создать папку"}

for key, value in command_menu.items():
    point = f'{key}: {value}'
    print(point)

command = int(input("Input number of the command above:"))

command_list = {1:open_dir, 2:list_dir, 3:del_one_dir, 4:add_one_dir}

if command != 2 and command <= 4:
    name = input("Input directory name:")
    command_list[command](name)
elif command > 4:
    print("Incorrect command!")
else:
    name = None
    command_list[command](name)
