"""Расчёт периметра и площади квадрата"""


__all__ = ['square_area', 'square_perimeter']

a = 15

'''Функция, расчитывающая периметр квадрата'''


def square_perimeter(x=a):
    return 4 * x


'''Функция, расчитывающая площадь квадрата'''


def square_area(x=a):
    return x ** 2
