# coding:utf-8
def fibonacci(n):
    # 递归终止条件
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        m = fibonacci(n - 1) + fibonacci(n - 2)
        return m


if __name__ == '__main__':
    print(fibonacci(5))
