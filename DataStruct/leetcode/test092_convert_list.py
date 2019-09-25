# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return None
        left, right = head, head
        stop = False

        # 链表无法回到上一个节点，采用递归来回溯right
        def recurseAndReverse(right, m, n):
            # 外层可用，left=left.next之后，上一层可用
            nonlocal left, stop
            # m和n可标识left和right是否到达目标位置
            if n == 1:
                return head
            right = right.next
            if m > 1:
                left = left.next

            recurseAndReverse(right, m - 1, n - 1)
            # 当left和right到达目标位置时，不再继续递归
            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next

        recurseAndReverse(right, m, n)
        return head

    # 迭代链表反转
    def reverseBetween01(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        cur, prev = head, None
        # prev和cur到达指定位置
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        tail, con = cur, prev

        # 完成链表反转操作
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # 调整
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


if __name__ == '__main__':
    node_list = input().strip().split(" ")
    m = int(input("m"))
    n = int(input("n"))
    next_node = None
    head_node = None
    for node in node_list[::-1]:
        head_node = ListNode(int(node))
        head_node.next = next_node
        next_node = head_node
    s = Solution()
    # head_node = s.reverseBetween(head_node, m, n)
    head_node = s.reverseBetween01(head_node, m, n)
    while head_node != None:
        print(head_node.val, "->", end="")
        head_node = head_node.next
