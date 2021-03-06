"""Напишите программу, которая выводит путь, по которому,
двигаясь интервалом длины m по заданному массиву, концом будет являться первый элемент.
Началом одного интервала является конец предыдущего. Путь - массив из начальных элементов полученных интервалов.
Пример 1:
n = 4, m = 3
Решение:
Круговой массив: 1234. При длине обхода 3 получаем интервалы: 123, 341. Полученный путь: 13.
Пример 2:
n = 5, m = 4
Решение:
Круговой массив: 123456. При длине обхода 4 получаем интервалы: 1234, 4512, 2345, 5123, 3451. Полученный путь: 14253.
Параметры передаются в качестве аргументов командной строки. Например, для последнего примера на вход подаются
аргументы: 5 4 Ожидаемый вывод в консоль: 14253
"""
import sys


def test(n, m):
    ans = [1, ]
    step = m - 1
    ind = step % n
    while ind != 0:
        ans.append(ind + 1)
        ind = (ind + step) % n
    return ''.join(map(str, ans))


if __name__ == '__main__':
    circ_arr = sys.argv[1]
    step = sys.argv[2]
    circ_arr = int(circ_arr)
    step = int(step)
    print(test(circ_arr, step))
