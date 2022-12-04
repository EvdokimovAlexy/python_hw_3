# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def creat_lst():
    a = [int(input('Введите значние\nnum= ')) for i in range(int(input('Введите количество символов\nlen = ')))]
    return a
num = creat_lst()
print(num)
mult = []
for i in range(0, (len(num) // 2 +1)):
    mult.append(num[i] * num[len(num) -i -1])
print(mult)