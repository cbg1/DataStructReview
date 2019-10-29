# coding:utf-8
'''给出二叉树的先序遍历和中序遍历，输出后序遍历'''

tree = input().split(" ")
pre = tree[0]
tin = tree[1]
aftree = []


def reconstruct(aftree, pre, tin):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return pre[0]
    # 取根节点
    aftree.append(pre[0])
    # 找到根节点在中序中的位置
    i = 0
    for i in range(len(tin)):
        if tin[i] == pre[0]:
            break
    # 根据中序中根节点位置将前序分成左右部分
    left_pre = pre[1:1 + i]
    right_pre = pre[1 + i:]
    # 根据中序中根节点位置将中序分成左右部分
    left_tin = tin[:i]
    right_tin = tin[i + 1:]
    # 然后对左右部分分别递归实现
    aftree.append(reconstruct(aftree, right_pre, right_tin))
    aftree.append(reconstruct(aftree, left_pre, left_tin))


# 12473568 47215386
# 74258631
reconstruct(aftree, pre, tin)
tmp = []
for i in aftree:
    if i != None:
        tmp.append(i)
res = ''.join(tmp)
print(res[::-1])
