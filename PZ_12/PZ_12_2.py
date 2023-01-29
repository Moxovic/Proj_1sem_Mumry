# Составить генератор (yield), который выводит из строки только буквы.
a = str(input('Введите строку: '))


def letters(words):
    for i in words:
        if i.isalpha():
            yield i


rom = [i for i in letters(a)]
print('Буквы из строки: ', *rom)
