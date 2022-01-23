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
