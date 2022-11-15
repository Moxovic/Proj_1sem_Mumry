import random  # Импортируем библиотеку random

n = random.randint(0, 10)
a = [random.randint(0, 10) for i in range(n)]  # Заполнение списка рандомными значениями
print(a)
for i in range(0, len(a)):  # Циклический сдвиг на одно значение влево
    a[i - 1] = a[i]
print(a)
