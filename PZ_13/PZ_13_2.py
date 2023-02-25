# В матрице найти минимальный элемент в предпоследней строке.

import random

a = random.randint(2, 8)
v = random.randint(2, 8)
moxovic = [[random.randint(-40, 40) for i in range(v)]for n in range(a)]
for i in moxovic:
    print(*i)
for g in range(v):
    min_el = min(moxovic[-2])
    print('\nМинимальный элемент с предпоследней строке :', min_el)
    break
