class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1:
            a = l1.val
            a = int(a)
            list1.append(a)
            l1 = l1.next
        while l2:
            b = l2.val
            b = int(b)
            list2.append(b)
            l2 = l2.next
        c = len(list1)
        d = len(list2)
        m = n = 0
        for i in range(c):
            m = m + list1[i] * (10 ** i)
        for j in range(d):
            n = n + list2[j] * (10 ** j)
        s = m + n
        s = str(s)
        curr = None
        last = None
        for h in s:
            curr = ListNode(h)
            curr.next = last
            last = curr

        return last


def creat_node_list(nums):
    dummy_node = ListNode(0)
    curr_node = dummy_node
    for num in nums:
        curr_node.next = ListNode(num)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    nums1 = [2, 4, 3]
    nums2 = [5, 6, 4]
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
