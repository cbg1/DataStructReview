# coding:utf-8
# 1.首先，判断这个数的最后一位是否为1，如果为1，那么计算器加1，然后通过右移丢弃掉最后一位，
# 2.循环执行该操作直到这个数等于0位置。
# 3.在判断二进制表示的最后一位是否为1时，采用与运算。

def count_bit(num):
    cnt = 0
    while num > 0:
        if num & 1 == 1:
            cnt += 1
        num >>= 1
    return cnt


def countOne(n):
    count = 0  # 用来计数
    while n > 0:
        if n != 0:
            n = n & (n - 1)
        count += 1
    return count


if __name__ == '__main__':
    # num = 18
    # print(count_bit(num))
    # print(countOne(num))
    print(7 >> 1)
