# coding:utf-8
'''
给定二叉树，从上往下逐层打印二叉树的节点的值，每层从左往右边
思路：广度优先遍历的实现，用队列实现
'''


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# 使用队列实现入队出队操作，打印成一行
def print_one_line(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# 上述基础上加入换行，打印出二叉树
def print_by_layer_1(root):
    if not root:
        return
    queue = []
    current_line = 0
    queue.append([current_line, root])
    while len(queue):
        line, node = queue.pop(0)
        if line != current_line:
            print()
            current_line = line
        print(node.val, end=" ")
        if node.left:
            queue.append([line + 1, node.left])
        if node.right:
            queue.append([line + 1, node.right])


# 3. 终极版
#    无line/current_line,在入队时候加入换行标记信息，注意边界条件，防止陷入死循环
def print_by_layer_2(root):
    if not root:
        return
    queue = ["r"]
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if isinstance(node, TreeNode):
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            if len(queue) > 0:
                queue.append("r")
                print()


def creat_bin_tree():
    # 新建节点
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)

    # 构建二叉树
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11

    # 指定 node1 为root节点
    root = node1

    return root


if __name__ == '__main__':
    root = creat_bin_tree()
    print_one_line(root)
    print("\n+++++++++++++++++++++++++")
    print_by_layer_1(root)
    print("\n+++++++++++++++++++++++++")
    print_by_layer_2(root)
