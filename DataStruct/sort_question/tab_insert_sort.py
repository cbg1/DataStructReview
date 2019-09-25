# coding:utf-8
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def table_insert_sort(node_list):
    node_list[0].next = 1
    node_list[1].next = 0
    for i in range(1, len(node_list)):
        q = 0
        p = node_list[0].next
        while p != 0 and node_list[i] >= node_list[p].val:
            q = p
            p = node_list[p].next

        node_list[i].next = p
        node_list[q].next = i


if __name__ == "__main__":
    nums = [312, 126, 272, 226, 28, 165, 123]
    node_list = []
    for i in range(len(nums)):
        node = Node(nums[i], None)
        node_list.append(node)
    table_insert_sort(node_list)
