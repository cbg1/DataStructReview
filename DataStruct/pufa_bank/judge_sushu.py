# coding:utf-8
# 大于1的自然数中除了1和本身之外不在有其他因数的自然数
def is_sushu(n):
    i = n
    if i < 2:
        return 0
    else:
        for i in range(n - 1, 1, -1):
            if n % i == 0:
                return 0
    return 1


if __name__ == '__main__':
    n = int(input())
    print(is_sushu(n))
