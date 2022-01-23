import sys


def find_point_pos(xc, yc, r, points_coordinates):
    for i in points_coordinates:
        x, y = i.split()
        x = float(x)
        y = float(y)
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

    find_point_pos(xc, yc, r, points_coordinates)
