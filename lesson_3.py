# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_full = [1, 1]
    fib = []
    itm = i = 1

    while itm <= m:
        i += 1
        itm = fib_full[i - 1] + fib_full[i - 2]
        fib_full.append(itm)
        if m >= itm >= n:
            fib.append(itm)

    return fib


f = fibonacci(5, 20)
print(f)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    inc = 0
    while inc < (len(origin_list) - 1):
        i = 0
        while i < (len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            i += 1
        inc += 1

    return (origin_list)


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def itr_filter(f_obj, itr):
    res = []
    res.append(f_obj(itr))
    return res


b = [1, 2, 7]
print(itr_filter(min, b))
print(itr_filter(max, b))
print(itr_filter(len, b))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def pgm(a1, a2, a3, a4):
    if (a1[1] == a4[1]) and (a2[1] == a3[1]) and (abs(a1[0] - a2[0]) == abs(a3[0] - a4[0])):
        res = "It's parallelogram"
    else:
        res = "It's not parallelogram"
    return res


check = pgm((1, 1), (2, 4), (7, 4), (6, 1))
print(check)
