# Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.
Letters = str(input())
Rus = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р",
       "с", "т", "у", "ф", "х", "ц", "ч", "ъ", "ы", "ь", "э", "ю", "я"]
Lat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = 0
for i in Letters:
    if i in Rus:
        n += 1
print("Количество русских букв :", n)
n = 0
for i in Letters:
    if i in Lat:
        n += 1
print("Количество латинских букв :", n)
