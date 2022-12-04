# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#  - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

import math
def creat_lst():
    a = [float(input('Введите значние\nnum= ')) for i in range(int(input('Введите количество символов\nlen = ')))]
    return a
num = creat_lst()
print(num)
b = []
for i in range(len(num)):
    b.append((num[i] % 1))
print(max(b) - min(b))