"""Расчёт периметра и площади треугольника"""


__all__ = ['triangle_perimeter', 'triangle_area']

from math import sqrt

a = 7
b = 2
c = 8

'''Функция, расчитывающая периметр треугольника'''


def triangle_perimeter(x=a, y=b, z=c):
    return x + y + z


'''Функция, расчитывающая площадь треугольника'''


def triangle_area(x=a, y=b, z=c):
    p = (x + y + z) / 2
    return sqrt(p * (p - x) * (p - y) * (p - z))
