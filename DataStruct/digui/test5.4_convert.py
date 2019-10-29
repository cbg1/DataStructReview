# coding:utf-8
# 将整数转换为字符串
def convert01(n):
    strs = ""
    while True:
        i = n // 10
        strs = str(n % 10) + strs
        n = i
        if i == 0:
            break
    return strs


def convert(n):
    i = n // 10
    if i != 0:
        strs = convert(i) + str(n % 10)
    else:
        strs = str(n % 10)
    return strs


if __name__ == '__main__':
    n = 456
    # strs = convert01(n)
    # print(strs)
    print(convert(n))
