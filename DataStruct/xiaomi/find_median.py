# coding:utf-8
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def find_mid_value(self, head):
        if not head:
            return None
        slow = quick = head
        while quick.next:
            if not quick.next.next:
                break
            slow = slow.next
            quick = quick.next.next

        if quick.next:
            return (slow.val + slow.next.val) / 2
        else:
            return slow.val


if __name__ == '__main__':
    node_list = input().strip().split(" ")
    next_node = None
    for node in node_list[::-1]:
        head_node = ListNode(int(node), next_node)
        next_node = head_node
    s = Solution()
    median = s.find_mid_value(head_node)
    print(median)
