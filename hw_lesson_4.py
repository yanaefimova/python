# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'

# Way 1
rsearch = r'[a-z]+'
result_re = re.findall(rsearch, line)
print(result_re)

# Way 2
result = ''
result_list = []
count_upper = 0
for itm in line:
    if itm.islower():
        result = result + itm
        count_upper = 0
    elif itm.isupper() and count_upper < 1:
        count_upper += 1
        result_list.append(result)
        result = ''

print(result_list)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'

# Way 1
# нужно получить список строк: ['AY', 'NOGI', 'P']

rsearch = r'(?<=[a-z]{2})[A-Z]+(?=[A-Z]{2})'
result_re = re.findall(rsearch, line)
print(result_re)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

with open("test.csv", "w", encoding="UTF-8") as doc:
    index_num = 1
    while index_num <= 2500:
        index_num += 1
        num = random.randint(0, 9)
        doc.write(str(num))

with open("test.csv", "r", encoding="UTF-8") as doc:
    big_num = str(doc.read())

itm = 0
list_dub = []
while itm < (len(big_num) - 1):
    val = 0
    if big_num[itm] == big_num[itm + 1]:
        i = itm
        val = str(big_num[i])
        while (big_num[i] == big_num[i + 1]) and itm < (len(big_num) - 1):
            val += str(big_num[i + 1])
            i += 1
            itm = i
    itm += 1
    list_dub.append(int(val))

max_len_num = max(list_dub)
out_str = f'Самая длинная последовательность одинаковых цифр {max_len_num}'
print(out_str)
