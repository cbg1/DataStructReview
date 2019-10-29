# 打印出图形
def myprint(n):
    # 递归终止条件
    if n == 0:
        return
    else:
        myprint(n - 1)
        for i in range(n):
            print(n, end=" ")
        print()


if __name__ == '__main__':
    myprint(5)
