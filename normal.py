__author__ = 'Никандров Владислав Павлович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

from random import randint
number, a = str(randint(0, 999999999)), 0

for i in number:
    if a < int(i):
        a = int(i)
    else:
        pass
print(number, 'Самая большая цифра это -', a)

# более короткая запись
from random import randint

number = str(randint(0,999999999))
number_dict = [i for i in number]
print(number, 'Самая большая цифра это -', max(number_dict))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

one, two = input('Введите первую переменную: '), input('Введите вторую переменную: ')

one, two = two, one

print('Поменяли переменные:\n', 'первая =', one, '\n', 'вторая =', two)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
from math import sqrt

print('Решаем ax² + bx + c = 0')

a,b,c = float(input('Введите a: ')), float(input('Введите b: ')), float(input('Введите c: '))
D = b ** 2 - 4 * a * c


if a != 0:
    x1 = (-b + sqrt(abs(D))) / (2 * a)
    x2 = (-b - sqrt(abs(D))) / (2 * a)
    print('Нет корней!') if D < 0 else print('x1 =', x1, 'x2 =', x2) if x1 != x2 else print('x =', x1)
else:
    print('a не может быть равна 0')


