# coding:utf-8
class node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


# 递归创建二叉树
def create_tree(nums, i):
    if i < len(nums):
        if nums[i] == None:
            return
        root = node(nums[i])
        root.lchild = create_tree(nums, 2 * i + 1)
        root.rchild = create_tree(nums, 2 * i + 2)
        return root


pre_series = []


# 前序遍历
def pre_order(root):
    if root:
        pre_series.append(root.data)
        pre_order(root.lchild)
        pre_order(root.rchild)


# 非递归前序遍历
def pre_order01(root):
    stack = []
    top = 0
    while root or top != 0:  # 子树不为空或者栈不为空
        if root:
            pre_series.append(root.data)
            stack.append(root)
            top += 1
            root = root.lchild
        else:
            root = stack.pop(len(stack) - 1)
            top -= 1
            root = root.rchild


in_series = []


# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        in_series.append(root.data)
        in_order(root.rchild)


# 非递归中序遍历
def in_order01(root):
    stack = []
    top = 0
    while root or top != 0:
        if root:
            stack.append(root)
            top += 1
            root = root.lchild
        else:
            root = stack.pop(len(stack) - 1)
            top -= 1
            in_series.append(root.data)
            root = root.rchild


post_series = []


# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        post_series.append(root.data)


class stack:
    def __init__(self):
        self.data = [None] * len(nums)
        self.tag = [None] * len(nums)


# 非递归后序遍历
def post_order01(root):
    s = stack()
    top = 0
    while root or top != 0:
        if root:
            s.data[top] = root
            s.tag[top] = 0
            top += 1
            root = root.lchild
        else:
            # 栈顶元素的tag为1，则栈顶元素出栈
            if s.tag[top - 1] == 1:
                top -= 1
                root = s.data[top]
                post_series.append(root.data)
                root = None
            # 如果栈顶元素的tag不为1则将其置一后遍历栈顶元素的右子树
            else:
                root = s.data[top - 1]
                s.tag[top - 1] = 1
                root = root.rchild


def pre_in_2_tree(pre_series, in_series):
    if len(pre_series) == 0:
        return 0
    elif len(in_series) == 1:
        return node(in_order(0))
    else:
        root = pre_series[0]
        mid = in_series.index(root)

        temp = node(root)
        temp.lchild = pre_in_2_tree(pre_series[1:mid + 1], in_series[:mid])
        temp.rchild = pre_in_2_tree(pre_series[mid + 1:], in_series[mid + 1:])
    return temp


if __name__ == '__main__':
    nums = ["a", "b", "c", "d", "f", None, None, None, "e", "g"]
    root = create_tree(nums, 0)
    # print("前序遍历:")
    # pre_order(root)
    # print(pre_series)
    # print("\n中序遍历:")
    # in_order(root)
    # print(in_series)
    # print("\n后序遍历:")
    # post_order(root)
    # print(post_series)
    # temp = pre_in_2_tree(pre_series, in_series)

    print("前序遍历:")
    pre_order01(root)
    print(pre_series)
    print("\n中序遍历:")
    in_order01(root)
    print(in_series)
    print("\n后序遍历:")
    post_order01(root)
    print(post_series)
