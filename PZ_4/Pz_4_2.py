# обработка исключений
try:
    n = int(input('Введите положительное значение: '))
    k = 0
    # условие на положительность
    if n <= 0:
        print('Error')
    else:
    # цикл по нахождению показателя степени числа 2
        while n != 2 ** k:
            # условие на проверку неравенства
            if 2 ** k != n:
                if k ** 2 > n:
                    print('Error')
                    break
                # если не подходит условию, то к степени прибавляется 1
                else:
                    k += 1
        # если введенное число равно 2 в степени k, то выводится показатель степени числа
        if n == 2 ** k:
            print(k)
except ValueError:
    print('Error')
