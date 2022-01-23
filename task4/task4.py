import statistics

a = [1, 10, 2, 9]

median = statistics.median(a)

print(int(sum(abs(v - median) for v in a)))

if __name__ == '__main__':
    pass