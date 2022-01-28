"""Напишите программу, которая рассчитывает положение точки относительно окружности.
Координаты центра окружности и его радиус считываются из файла1.
Пример:
1 1
5
Координаты точек считываются из файла2.
Пример:
0 0
1 6
6 6
Файлы передаются программе в качестве аргументов. Файл с координатами и радиусом окружности - 1 аргумент,
файл с координатами точек - 2 аргумент.
Координаты в диапазоне float.
Количество точек от 1 до 100.
Вывод каждого положения точки заканчивается символом новой строки.
Соответствия ответов:
0 - точка лежит на окружности 1 - точка внутри
2 - точка снаружи
"""
import sys


def find_point_pos(xc, yc, r, x, y):
    if ((x - xc) * (x - xc) + (y - yc) * (y - yc)) < r * r:
        print(1)
    elif ((x - xc) * (x - xc) + (y - yc) * (y - yc)) == r * r:
        print(0)
    else:
        print(2)


if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    with open(file1) as f:
        c = f.readline()
        r = f.readline()

    xc, yc = c[0], c[2]
    xc = float(xc)
    yc = float(yc)
    r = float(r)

    with open(file2) as f:
        points_coordinates = f.readlines()
        for point in points_coordinates:
            x, y = point.split()
            x = float(x)
            y = float(y)
            find_point_pos(xc, yc, r, x, y)
