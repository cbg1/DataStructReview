# coding:utf-8
class node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def is_palinrome(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    if (len(res) <= 1):
        return True
    else:
        n = len(res)
        for i in range(n // 2):
            if res[i] != res[n - i - 1]:
                return False
        return True


if __name__ == '__main__':
    val_list = list(map(int, input().strip().split(" ")))
    next_node = None
    current_node = None
    for val in val_list[::-1]:
        current_node = node(val, next_node)
        next_node = current_node
    head = current_node
    result = is_palinrome(head)
    print(result)
