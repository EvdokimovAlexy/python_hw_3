# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def creat_lst():
    a = [int(input('Введите значние\nnum= ')) for i in range(int(input('Введите количество символов\nnum= ')))]
    return a
num = creat_lst()
print(num)
summa = 0
for i in range(len(num)):
    if i % 2 == 1:
        summa = summa + num[i]
print(f'Сумма чисел на нечетных позициях = ', summa)