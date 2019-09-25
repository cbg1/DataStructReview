# coding:utf-8
# 实现二叉树的逐层打印


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_b_tree(tree_list, i):
    if i < len(tree_list):
        if tree_list[i] == None:
            return
        root = TreeNode(tree_list[i])
        root.left = create_b_tree(tree_list, 2 * i + 1)
        root.right = create_b_tree(tree_list, 2 * i + 2)
        return root


def print_level_tree(root):
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


# 控制换行
def print_level_tree01(root):
    if not root:
        return
    queue = []
    current_line = 0
    queue.append([current_line, root])
    while len(queue) > 0:
        line, node = queue.pop(0)
        if line != current_line:
            print()
            current_line = line
        print(node.val, end=" ")
        if node.left:
            queue.append([line + 1, node.left])
        if node.right:
            queue.append([line + 1, node.right])


# 控制换行
def print_level_tree02(root):
    if not root:
        return
    queue = ["r1"]
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
                if node != "r1":
                    print()


if __name__ == '__main__':
    # data = [3, 9, 20, None, None, 15, 7]
    data = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = create_b_tree(data, 0)
    # print_level_tree(root)
    # print_level_tree01(root)
    print_level_tree02(root)
