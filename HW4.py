# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#     print(f"Число {num} в двоичной системе это {binum})

num = int(input('Введите десятичное число: '))
num1 = num
binum = ''
while num1 > 0:
    binum = str(num1 % 2) + binum
    num1 //= 2
 
print(f"Число {num} в двоичной системе это {binum}")