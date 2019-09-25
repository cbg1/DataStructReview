# coding:utf-8
import time


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 从上至下暴力法
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    # 从下至上提前阻断法,从下至上，如果发现有一个不符合，则一路传递-1
    # 避免后续对于的计算
    def isBalanced01(self, root: TreeNode) -> bool:
        return self.depth01(root) != -1

    def depth01(self, root):
        if not root:
            return 0
        left = self.depth01(root.left)
        if left == -1:
            return -1
        right = self.depth01(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1


def create_b_tree(tree_list, i):
    if i < len(tree_list):
        if tree_list[i] == None:
            return
        root = TreeNode(tree_list[i])
        root.left = create_b_tree(tree_list, 2 * i + 1)
        root.right = create_b_tree(tree_list, 2 * i + 2)
        return root


if __name__ == '__main__':
    time_start = time.time()
    # data = [3, 9, 20, None, None, 15, 7]
    data = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = create_b_tree(data, 0)
    s = Solution()
    # print(s.isBalanced(root))
    print(s.isBalanced01(root))  # spend time: 0.0009968280792236328
    time_end = time.time()
    print("spend time:", time_end - time_start)
