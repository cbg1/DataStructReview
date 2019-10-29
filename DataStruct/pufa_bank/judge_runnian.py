# coding:utf-8
# 闰年：能被4且不能被100整数或者能被400整除
def is_runnian():
    for i in range(1990, 2011):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            print(i, end=" ")


if __name__ == '__main__':
    is_runnian()
