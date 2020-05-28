# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1

if b > 0:
    print(f'Формула выглядит y = {k}x + {b}')
else:
    b = abs(b)
    print(f'Формула выглядит y = {k}x - {b}')