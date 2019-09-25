# 打印出图形
def myprint(n):
    if n != 0:
        myprint(n - 1)
        for i in range(n):
            print(n, end=" ")
        print()


if __name__ == '__main__':
    myprint(5)
