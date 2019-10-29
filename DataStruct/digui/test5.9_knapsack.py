# coding:utf-8
# 简单背包问题，w1,w2...wm中选取若干件物品重量等于s,优先考虑重量大的物品
# 由大到小，先判断wm是否可选，s-wm是否满足
# 递归实现
def knapsack(s, m):
    # 递归终止的条件
    if s == 0:
        return True
    elif s < w[0] or m == -1:
        return False
    else:
        while True:
            s1 = w[m]
            m -= 1
            b = knapsack(s - s1, m)
            if m == -1 or b:
                break
        if not b:
            return False
        else:
            # 将选出的物品重量打印出来
            print(s1, end=" ")
            return True


class stackelem:
    def __init__(self, ss, mm):
        self.ss = ss
        self.mm = mm


# 非递归实现
def knapsack01(s, m):
    t = 0  # 记录当前已被选物品总和
    top = 0
    nofail = 1
    stack = []
    # 背包重没用完，或者不失败
    while s != t and nofail:
        # 至少还有一个物品可选
        if s > t + w[0] and m > -1:
            # 选择m并且栈
            stack.append(stackelem(w[m], m))
            top += 1
            t = t + w[m]
            m -= 1
        # 表示刚才的一个选择不合适，需要回溯
        else:
            # 弹出栈顶元素
            if m == -1:
                top -= 1
                t = t - stack.pop().ss
            # 栈空了
            if top < 1:
                nofail = 0
            # 弹出栈顶元素，并且向前一个元素开始试探
            else:
                top -= 1
                top_elem = stack.pop()
                m = top_elem.mm - 1
                t = t - top_elem.ss
    if s == t:
        while len(stack) > 0:
            print(stack.pop().ss, end=" ")
    else:
        print("their is no any selection")


if __name__ == '__main__':
    w = [1, 2, 3, 4, 5]
    n = len(w)
    # knapsack(10, n - 1)
    knapsack01(85, n - 1)
