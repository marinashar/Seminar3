# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
N = int(input('Введите размер списка: '))
lst = []
for i in range (N):
    lst.append(random.randint(0, 10))
print(lst)

def GetSumOdd(lst):
    summa = 0
    for i in range (len(lst)):
        if i % 2 != 0:
            summa += lst[i]
    print(f"Сумма чисел на нечетных позициях элементов равна {summa}")
GetSumOdd(lst)
