"""1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень"""

months = int(input("Введите номер месяца: "))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if months == 1 or months == 2 or months == 12:
    print("Результат через список: ", seasons_list[0])
    print("Результат через список: ", seasons_dict.get(1))
elif months == 3 or months == 4 or months == 5:
    print("Результат через список: ", seasons_list[1])
    print("Результат через список: ", seasons_dict.get(2))
elif months == 6 or months == 7 or months == 8:
    print("Результат через список: ", seasons_list[2])
    print("Результат через список: ", seasons_dict.get(3))
elif months == 9 or months == 10 or months == 12:
    print("Результат через список: ", seasons_list[3])
    print("Результат через список: ", seasons_dict.get(4))
else:
    print("Такого месяца нет")