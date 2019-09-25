# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 迭代链表反转
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        # 先移动到指定位置
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1
            n -= 1
        tail, con = curr, prev
        # 从指定位置开始进行反转
        while n:
            third = curr.next
            curr.next = prev
            
            prev = curr
            curr = third
            n -= 1

        # 调整节点
        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr
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
    head_node = s.reverseBetween(head_node, m, n)
    while head_node != None:
        print(head_node.val, "->", end="")
        head_node = head_node.next
