"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

list_new = list(input("Введите целые числа через пробел: "))
print (''.join(list_new))
for i in range(0, len(list_new)-1, 2):
    list_new[i], list_new[i+1] = list_new[i+1], list_new[i]
print (''.join(list_new))
