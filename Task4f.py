# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

a = int(input('Введите сколько журавликов дети сделали вместе: '))
ps_crane = a / 5
k_crane = (ps_crane + ps_crane) * 2
print(f"Петя и Серёжа сделали по {ps_crane} шт., а Катя сделала {k_crane}")
