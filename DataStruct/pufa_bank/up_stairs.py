# coding:utf-8
# 有n步台阶，一次只能上1步或2步，共有多少种走法

# 递归
def up_stairs(n):
    if n <= 2:
        return n
    x = up_stairs(n - 1) + up_stairs(n - 2)
    return x


# 迭代
def up_stairs01(n):
    if n <= 2:
        return n
    first = 1
    second = 2
    third = 0
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return third


# 动态规划
def up_stairs02(n):
    a = [0] * 100
    if n <= 2:
        a[n] = n
    if a[n] > 0:
        return a[n]
    else:
        a[n] = up_stairs02(n - 1) + up_stairs02(n - 2)
        return a[n]


if __name__ == '__main__':
    print(up_stairs(3))
    print(up_stairs01(3))
    print(up_stairs02(3))
