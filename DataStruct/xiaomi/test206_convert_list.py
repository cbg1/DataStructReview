# coding:utf-8
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    # 迭代
    def reverseBetween(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        while curr != None:
            # 反转
            temp = curr.next
            curr.next = prev
            # 整体向后移动
            prev = curr
            curr = temp
        return prev

if __name__ == '__main__':
    node_list = input().strip().split(" ")
    next_node = None
    head_node = None
    for node in node_list[::-1]:
        head_node = ListNode(int(node), next_node)
        next_node = head_node
    s = Solution()
    head_node = s.reverseBetween(head_node)
    while head_node != None:
        print(head_node.val, "->", end="")
        head_node = head_node.next
