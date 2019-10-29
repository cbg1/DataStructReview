# coding:utf-8
def fact(n):
    # 递归终止条件
    if n == 0:
        return 1
    else:
        m = n * fact(n - 1)
        return m


if __name__ == '__main__':
    n = 5
    print(fact(n))
