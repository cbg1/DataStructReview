# coding:utf-8
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_list(head):
    pass


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(" ")))
    next = None
    head = None
    for num in nums[::-1]:
        head = Node(num)
        head.next=next
        next=head
