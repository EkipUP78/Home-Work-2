'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5

Вывести цифры числа на каждой новой строке.

Пример:
     123567

     1
     2
     3
     4
     5
     6
     7

'''
str_5 = str(input('Введите любое целое цисло: '))
print('-' * 18)
print('Вы ввели число:', str_5)

for elem in str_5:
    print(' ' * 15, elem)