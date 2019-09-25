# coding:utf-8
# 非递归解法根据递推式自下而上进行
def Fact01(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


# 递归是自上而下递归调用，避免许多重复计算
def Fact(n):
    if n == 1:
        return 1
    else:
        return n * Fact(n - 1)


if __name__ == '__main__':
    print(Fact(3))
