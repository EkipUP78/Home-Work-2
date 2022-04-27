'''
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''

number = 0
for i in range(1,11):
    digit_input = int(input('Введите с клавиатуры произвольную цифру: ',))
    if digit_input == 5:
        number = number + 1

print('-' * 42)

if number > 0:
    if number % 10 == 1:
        print('Введена', number, 'цифра 5')
    elif 2 <= number % 10 <= 4:
        print('Введено', number, 'цифры 5')
    elif 5 <= number % 10 <= 9 or number % 10 == 0:
        print('Введено', number, 'цифр 5')
else:
    print('Введено', number, 'цифр 5')