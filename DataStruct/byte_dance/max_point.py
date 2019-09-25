# coding:utf-8
from functools import cmp_to_key


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cmp(a: Point, b: Point):
    if a.y == b.y:
        return a.x > b.x
    else:
        return a.y < b.y


def max_point(count, points):
    filters = []
    cur_max_rank = 0
    cur_max_index = 0
    for i in range(count):
        temp = points[i].x + points[i].y - abs(points[i].x - points[i].y)
        if temp > cur_max_rank:
            cur_max_rank = temp
            cur_max_index = i
    f_count = 0
    for i in range(count):
        if points[i].x > points[cur_max_index].x or points[i].y >= points[cur_max_index].y:
            filters.append(points[i])
            f_count += 1
    filters = list(sorted(filters, key=cmp_to_key(cmp)))

    maxx = -1
    for i in range(f_count):
        if filters[i].x > maxx:
            print(filters[i].x, filters[i].y)


# 所有y值大于该点的y值的点的x值都小于该点x，则该点为最大点

if __name__ == '__main__':
    count = int(input())
    points = []
    result = []
    for i in range(0, count):
        point_str = input().strip().split(" ")
        point = Point(int(point_str[0]), int(point_str[1]))
        points.append(point)
    max_point(count, points)
