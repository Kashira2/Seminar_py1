# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Введите X координату первой точки: '))
y1 = float(input('Введите Y координату первой точки: '))
x2 = float(input('Введите X координату второй точки: '))
y2 = float(input('Введите Y координату второй точки: '))

import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'Расстояние между двумя точками равна {round(distance, 2)}')