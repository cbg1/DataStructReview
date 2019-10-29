# coding:utf-8
'''
合并两个有序链表
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        l3 = dummy
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return dummy.next


def print_list(head):
    while head:
        if head.next:
            print(head.val, end="->")
        else:
            print(head.val, end="\n")
        head = head.next


if __name__ == '__main__':
    nums1 = [1, 2, 4]
    nums2 = [1, 3, 4]

    dummy1 = ListNode(0)
    p1 = dummy1
    for num in nums1:
        p1.next = ListNode(num)
        p1 = p1.next
    l1 = dummy1.next

    dummy2 = ListNode(0)
    p2 = dummy2
    for num in nums2:
        p2.next = ListNode(num)
        p2 = p2.next
    l2 = dummy2.next
    s = Solution()
    print_list(s.mergeTwoLists(l1, l2))
