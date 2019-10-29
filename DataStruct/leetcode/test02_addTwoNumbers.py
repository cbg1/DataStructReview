# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        p = l1
        q = l2
        carry = 0
        while p and q:
            temp = p.val + q.val + carry
            carry = temp // 10
            curr.next = ListNode(temp % 10)
            curr = curr.next
            p = p.next
            q = q.next

        while p:
            temp = p.val + carry
            carry = temp // 10
            curr.next = ListNode(temp % 10)
            curr = curr.next
            p = p.next

        while q:
            temp = q.val + carry
            carry = temp // 10
            curr.next = ListNode(temp % 10)
            curr = curr.next
            q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head.next


def creat_node_list(nums):
    dummy_node = ListNode(0)
    curr_node = dummy_node
    for num in nums:
        curr_node.next = ListNode(num)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    nums1 = [1, 8]
    nums2 = [0]
    l1 = creat_node_list(nums1)
    l2 = creat_node_list(nums2)
    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    while l3:
        if l3.next:
            print(l3.val, end="->")
        else:
            print(l3.val, end="")
        l3 = l3.next
