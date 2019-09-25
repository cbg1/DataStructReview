# coding:utf-8
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_list(head):
    if not head:
        return None
    pre = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = pre

        pre = curr
        curr = temp
    return pre


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(" ")))
    last = None
    head = None
    for num in nums[::-1]:
        head = Node(num)
        head.next = last
        last = head
    convert_list(head)

