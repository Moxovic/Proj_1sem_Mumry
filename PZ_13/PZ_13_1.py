# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

import random

a = random.randint(2, 8)
v = random.randint(2, 8)
print('Исходная матрица : ')
moxovic = [[random.randint(-40, 40) for i in range(v)]for n in range(a)]
for i in moxovic:
    print(*i)
bang = []
print('\n')
for i in range(0, v):
    sum1 = 0
    for g in moxovic:
        sum1 += g[i]
    bang.append(sum1)
    print("Сумма элементов столбца :", sum1)
print('\n')
moxovic[1] = bang
print('Новая матрица :')
for i in moxovic:
    print(*i)
