"""Расчёт периметра и площади круга"""


__all__ = ['circle_area', 'circle_perimeter']

from math import pi

default_radius = 5

'''Функция, расчитывающая длину окружности'''


def circle_perimeter(r=default_radius):
    return 2 * pi * r


'''Функция, расчитывающая площадь окружности'''


def circle_area(r=default_radius):
    return pi * r ** 2
