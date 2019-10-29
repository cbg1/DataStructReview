# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 两次遍历，第一次记录链表节点个数，第二遍寻找目标点
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length, p = 0, head
        while p:
            length += 1
            p = p.next
        length -= n
        p = dummy
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
        # 根据实际情况来走
        for i in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    nums = [1]
    n = 1
    head = None
    next = None
    for num in nums[::-1]:
        head = ListNode(num)
        head.next = next
        next = head
    s = Solution()
    head = s.removeNthFromEnd01(head, n)
    while head:
        print(head.val, end="->")
        head = head.next
