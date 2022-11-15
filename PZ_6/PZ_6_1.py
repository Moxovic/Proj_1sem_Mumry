import random  # Импортируем библиотеку random

n = random.randint(1, 10)
a = [i for i in range(n)]  # Заполнение списка рандомными значениями
for i in range(len(a) // 2):  # Выводятся элементы в последовательности A1, AN, A2, AN-1, A3, AN-2, …
    print(a[i])
    print(a[len(a) - i - 1])
