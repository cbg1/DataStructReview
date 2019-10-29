# coding:utf-8
# 求最大公约数,辗转相除法，直到余数为0则为止
def gcd(m, n):
    # 一定要保持m>n
    if n > m:
        return gcd(n, m)
    if n == 0:
        return m
    else:
        k = m % n
        return gcd(n, k)


if __name__ == '__main__':
    print(gcd(2, 3))
