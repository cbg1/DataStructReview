# coding:utf-8

'''
输入N, 打印 N*N 螺旋矩阵
比如 N = 3，打印：
1 2 3
8 9 4
7 6 5
N = 4，打印：
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''


def generate_mat(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    l, r, t, b = 0, n - 1, 0, n - 1
    num = 1
    while num <= n * n:
        # 从左往右
        for i in range(l, r + 1):
            mat[t][i] = num
            num += 1
        t += 1
        # 从上往下
        for i in range(t, b + 1):
            mat[i][r] = num
            num += 1
        r -= 1
        # 从右往左
        for i in range(r, l - 1, -1):
            mat[b][i] = num
            num += 1
        b -= 1
        # 从下往左
        for i in range(b, t - 1, -1):
            mat[i][l] = num
            num += 1
        l += 1
    return mat


if __name__ == '__main__':
    n = int(input("N"))
    mat = generate_mat(n)
    for i in range(n):
        print(mat[i])
