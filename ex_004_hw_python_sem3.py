# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
num = int(input('Введите десятичное число = '))

binary = ''

while num > 0:
    binary = str(num % 2) + binary
    num = num // 2

print(f'Бинарный код', binary)