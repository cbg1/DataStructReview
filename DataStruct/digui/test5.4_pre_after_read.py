class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def p_left_2_right(head):
    if head.next:
        print(head.next.data, end="->")
        p_left_2_right(head.next)


def p_right_2_left(head):
    if head.next:
        p_right_2_left(head.next)
        print(head.next.data, end="->")


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    dummy = LinkNode(0)
    curr = dummy
    for num in nums:
        curr.next = LinkNode(num)
        curr = curr.next
    p_left_2_right(dummy)
    print()
    p_right_2_left(dummy)
