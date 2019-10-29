# coding:utf-8
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_list(head):
    if not head:
        return
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# 反转链表的递归实现
def convert_list01(head):
    if not head or not head.next:
        return head
    p = convert_list01(head.next)
    head.next.next = head
    head.next = None
    return p


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(" ")))
    last = None
    head = None
    for num in nums[::-1]:
        head = Node(num)
        head.next = last
        last = head
    # head = convert_list(head)
    head = convert_list01(head)
    while head:
        print(head.val, end=" ")
        head = head.next
