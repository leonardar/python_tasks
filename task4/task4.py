"""
Дан массив целых чисел nums. Напишите программу, выводящую минимальное количество ходов,
требуемых для приведения всех элементов к одному числу. За один ход можно уменьшить или увеличить число массива на 1.
Пример:
nums = [1, 2, 3]
Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2] Минимальное количество ходов: 2
Элементы массива читаются из файла, переданного в качестве аргумента командной строки.
Пример:
1
10
2
9
На вход подаётся файл с содержимым:
Вывод в консоль: 16
"""
import statistics
import sys

f_n = sys.argv[1]


def num_equalize(file):
    nums_list = []
    with open(file) as file:
        nums = file.readlines()
        for i in nums:
            nums_list.append(int(i))

    median = statistics.median(nums_list)
    result = (int(sum(abs(v - median) for v in nums_list)))
    print(result)


if __name__ == '__main__':
    num_equalize(f_n)
