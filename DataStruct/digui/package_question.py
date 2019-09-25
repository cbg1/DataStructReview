# coding:utf-8
# 从w1,w2,w3。。。wm中选择若干物品，总和等于s，是否存在解
#物品升序存储，优先选最大的
# 递归实现
def knapsack1(s, m, w):
    if s == 0:
        return 1
    elif s < w[0] or m == 0:
        return 0

    else:
        while True:
            s1 = w[m]
            m -= 1
            print(s1, m)
            b = knapsack1(s - s1, m, w)
            if b or m == 0:
                break
        # b为0,不成立
        if not b:
            return 0
        else:
            print(s1, end=" ")
            return 1
# 非递归实现
def knapsack2(s, m, w):
    pass

if __name__ == '__main__':
    w = [1, 2, 3, 4, 5]
    s = 10
    print("result:", knapsack1(s, len(w) - 1, w))
