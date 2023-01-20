# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:
import random

f1 = open(file='moxovic1.txt', mode='w', encoding='UTF-8')
rom = [random.randint(-12, 12) for i in range(random.randint(6, 13))]
f1.write(str(rom))
f1.close()


f2 = open(file='moxovic2.txt', mode='w', encoding='UTF-8')
f2.write(f'Исходные данные: {rom}\n')
f2.write(f'Кол-во элементов: {len(rom)}\n')
last_minimal = len(rom) - rom[::-1].index(min(rom)) - 1
f2.write(f'Индекс последнего минимального элемента: {last_minimal}\n')
ymnoj = list(map(lambda x: x * rom[0], rom))
f2.write(f'Умножаем все элементы на первый элемент: {ymnoj}')
f2.close()
