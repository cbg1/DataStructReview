# coding:utf-8
'''
解法1：两次遍历，先获取链表节点个数，再遍历寻找到倒数第n个点
解法2：双指针，先first走n步，再first和second一起走知道first到最后，second即为倒数第n个节点
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 两次遍历，第一次记录链表节点个数，第二遍寻找目标点
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        length = 0
        while head:
            length += 1
            head = head.next
        length -= n
        while length > 0:
            length -= 1
            p = p.next
        p.next = p.next.next
        return dummy.next

    # first先走n步，然后first和second一起走到底，second为所求
    def removeNthFromEnd01(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        while n:
            n -= 1
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    n = 2
    dummy = ListNode(0)
    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    head = dummy.next
    s = Solution()
    # head = s.removeNthFromEnd(head, n)
    head = s.removeNthFromEnd01(head, n)
    while head:
        if head.next:
            print(head.val, end="->")
        else:
            print(head.val, end="")
        head = head.next
