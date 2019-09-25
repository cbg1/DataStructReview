# coding:utf-8
MAXSIZE = 100


# 双亲表示法
class node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent


class tree:
    def __init__(self, tree_list, length, root):
        self.tree_list = tree_list
        self.length = length
        self.root = root


# 孩子表示法
class node:
    def __init__(self, data, child):
        self.data = data
        self.child = child
