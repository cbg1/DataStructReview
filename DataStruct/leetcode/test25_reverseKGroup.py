# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        end = dummy

        while end.next:
            i = 0
            while i < k and end:
                i += 1
                end = end.next
            if end == None:
                break

            start = pre.next
            temp = end.next
            end.next = None

            pre.next = self.reverse(start)
            start.next = temp

            pre = start
            end = pre
        return dummy.next

    def reverse(self, head):
        pre = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = pre

            pre = curr
            curr = temp
        return pre


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = 3
    head = None
    next = None
    for num in nums[::-1]:
        head = ListNode(num)
        head.next = next
        next = head
    s = Solution()
    res_head = s.reverseKGroup(head, k)
    while res_head:
        if res_head.next:
            print(res_head.val, end="->")
        else:
            print(res_head.val, end="")
        res_head = res_head.next
