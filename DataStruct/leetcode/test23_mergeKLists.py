# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 暴力法,取出所有链表中的num，排序结果数组，生成结果链表
    def mergeKLists(self, lists):
        merged_list = []
        for list in lists:
            head = list
            while head:
                merged_list.append(head.val)
                head = head.next
        merged_list.sort()
        res_head = None
        next = None
        for merged_num in merged_list[::-1]:
            res_head = ListNode(merged_num)
            res_head.next = next
            next = res_head
        return res_head

    # 取链表的z最小首个节点比较进入新链表即可
    def mergeKLists01(self, lists):
        nums = []
        # 当lists中还有不为空的head时
        while lists.count(None) < len(lists):
            new_lists = [head for head in lists if head != None]
            min_val = new_lists[0].val
            min_index = 0
            for index, head in enumerate(new_lists):
                if head.val < min_val:
                    min_val = head.val
                    min_index = index

            new_lists[min_index] = new_lists[min_index].next
            lists = new_lists
            nums.append(min_val)

        res_head = None
        res_next = None
        for num in nums[::-1]:
            res_head = ListNode(num)
            res_head.next = res_next
            res_next = res_head
        return res_head

    # 取链表的z最小首个节点比较进入新链表即可
    def mergeKLists02(self, lists):
        length = len(lists)
        interval = 1
        # 最后一次归并前肯定小于，归并后大于
        while interval < length:
            for i in range(0, length - interval, 2 * interval):
                lists[i] = self.merge2list(lists[i], lists[i + interval])
                interval = interval * 2
        return lists[0] if length > 0 else lists

    def merge2list(self, l1, l2):
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next


if __name__ == '__main__':
    nums_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for nums in nums_list:
        head = None
        next = None
        for num in nums[::-1]:
            head = ListNode(num)
            head.next = next
            next = head
        lists.append(head)
    s = Solution()
    # head = s.mergeKLists(lists)
    # head = s.mergeKLists01(lists)
    head = s.mergeKLists02(lists)
    while head:
        print(head.val, end="->")
        head = head.next
