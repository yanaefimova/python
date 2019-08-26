__author__ = 'Efimova Yana'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('Hello!\nEnter some number:')
num_value = input()
i = 0
max_num_value = int(num_value[i])
while i <= (len(num_value)-1):
    if int(num_value[i]) > max_num_value:
        max_num_value = int(num_value[i])
    i += 1
print('The maximum value from the number is', max_num_value)




# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# first_value = int(input('Hello!\nEnter the first value:'))
# second_value = int(input('Enter the second value:'))
#
# first_value = first_value + second_value
# second_value = first_value - second_value
# first_value = first_value - second_value
#
# print('\nThe first inverted value -', first_value)
# print('The second inverted value -', second_value)

# Вариант 2

# first_value = input('Hello!\nEnter the first value:')
# second_value = input('Enter the second value:')
#
# first_value, second_value = second_value, first_value
#
# print('\nThe first inverted value -', first_value)
# print('The second inverted value -', second_value)




# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# import math
# print('ax² + bx + c = 0')
# a = int(input('Enter A value:'))
# b = int(input('Enter the B value:'))
# c = int(input('Enter the C value:'))
#
# D = b**2-4*a*c
#
# if D < 0:
#     print('D < 0: There is no solution')
# elif D == 0:
#     x = -b/2*a
#     print('D = 0: X=', x)
# else:
#     x1 = round((-b+math.sqrt(D))/(2*a), 2)
#     x2 = round((-b-math.sqrt(D))/(2*a), 2)
# print('D > 0: X1=', x1, 'X2=', x2)