# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 递归法
    '''
    1.使用的同一种方式做相邻节点交换
    2.递归终止条件为head.next为空
    ps:判断head是否为none
    '''

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        curr = head.next
        head.next = self.swapPairs(head.next.next)
        curr.next = head
        return curr

    # 非递归法
    def swapPairs01(self, head):
        pre = ListNode(0)
        pre.next = head
        temp = pre
        while temp.next and temp.next.next:
            # 在点调用之前不能修改点
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        return pre.next


def print_link_list(head):
    while head:
        if head.next:
            print(head.val, end="->")
        else:
            print(head.val, end="\n")
        head = head.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # 逆序创建链表
    # head = None
    # next = None
    # for num in nums[::-1]:
    #     head = ListNode(num)
    #     head.next = next
    #     next = head
    # 正序创建链表
    dummy = ListNode(0)
    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    head = dummy.next
    print_link_list(head)
    s = Solution()
    res_head = s.swapPairs(head)
    # res_head = s.swapPairs01(head)
    print_link_list(res_head)
