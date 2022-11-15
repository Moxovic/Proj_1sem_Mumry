import random  # Импортируем библиотеку random

n = random.randint(1, 10)
b = 0
a = [random.randint(1, 5) for i in range(n)]  # Заполнение списка рандомными значениями
a.sort()  # Сортирует список в порядке возрастания
print(a)
for i in a:  # Подсчёт неповторяющихся значений
    if a.count(i) == 1:  # Подсчитывает количество вхождений элемента в списке
        b += 1
    else:
        continue
print(b)
