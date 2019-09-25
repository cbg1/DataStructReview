# coding:utf-8
'''O(n*n)'''
'''稳定算法'''
'''从数的低位开始向高位排序'''
B = 5
f = [0] * 10
e = [0] * 10


class Node:
    def __init__(self, key, link):
        self.key = key
        self.link = link


# 根据排序码分配
def distribute(r, i):
    p = r[0].link
    while p:
        # # 第i个排序码
        j = r[p].key[i]
        if not f[j]:
            f[j] = p
        else:
            r[e[j]].link = p
        e[j] = p
        # 继续指向下一个节点
        p = r[p].link


def collect(r):
    j = 0
    while not f[j]:
        j += 1
    r[0].link = f[j]
    t = e[j]
    while j < 9:
        j += 1
        while j < 9 and not f[j]:
            j += 1
        if f[j]:
            r[t].link = f[j]
            t = e[j]
    r[t].link = 0


# 升序排序
def radix_sort(r):
    for i in range(2):
        # # 分配和收集
        distribute(r, i)
        collect(r)
        print("i:", i, "排序收集后:")
        for i in r:
            print("key:", i.key, "link:", i.link)

        # p = r[0].link
        # while p:
        #     print(r[p].key, end=" ")
        #     p = r[p].link
        #     print(p)
        # print("")


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 8, 165, 123, 12, 28]
    node = Node(None, None)
    r = [node] * (len(nums) + 1)
    r[0].link = 1
    for index, num in enumerate(list(nums)):
        key = [0] * B
        for i in range(len(str(num))):
            key[i] = int(list(str(num))[len(str(num)) - 1 - i])
        r[index + 1] = Node(key, index + 2)
    r[len(nums)].link = 0
    print("排序前")
    p = r[0].link
    while p:
        print(r[p].key, end=" ")
        p = r[p].link
    print("")

    num_sorted = radix_sort(r)
    # print(num_sorted)
