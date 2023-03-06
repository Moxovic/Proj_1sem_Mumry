from figures import circle_perimeter
from figures import circle_area
from figures import triangle_perimeter
from figures import triangle_area
from figures import square_perimeter
from figures import square_area
from figures import circle
from figures import triangle
from figures import square
print(circle.code.__doc__)
print(square.code.__doc__)
print(triangle.code.__doc__)
print('Длина окружности: ', circle_perimeter())
print('Площадь окружности: ', circle_area(5))
print('Периметр треугольника: ', triangle_perimeter(7, 3, 9))
print('Площадь треугольника: ', triangle_area())
print('Периметр квадрата: ', square_perimeter(6))
print('Площадь квадрата: ', square_area())
