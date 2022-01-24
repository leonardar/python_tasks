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
