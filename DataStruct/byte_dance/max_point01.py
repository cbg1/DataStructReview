# coding:utf-8
from functools import cmp_to_key

MAXN = int(5e5 + 10)  # s设置上限


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cmp(a: point, b: point):
    return a.x < b.x


def solve(pts, res, n):
    pts = list(sorted(pts, key=cmp_to_key(cmp)))  # 按照x由小到大排序
    res[0] = pts[n - 1]  # 最右点绝对在最大点集中
    mx = res[0].y
    cnt = 1  # 最大点集数
    # 从右边往左边扫描，如果y大于历史最大y值，则改点在最大点集中
    for i in range(n - 2, -1, -1):
        if pts[i].y >= mx:
            res[cnt] = pts[i]  # 更新最大点集
            cnt += 1
            mx = pts[i].y  # 更新历史最大y值
    return res, cnt


if __name__ == '__main__':
    n = int(input())
    pts = [[] for _ in range(MAXN)]
    res = []
    for i in range(n):
        point_str = input().strip().split(" ")
        pts[i] = point(int(point_str[0]), int(point_str[1]))
    result, cnt = solve(pts, res, n)
    for i in range(cnt):
        print(result[i].x, result[i].y)
