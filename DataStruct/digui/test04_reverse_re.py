# coding:utf-8
def reverse(l, left, right):
    if left < right:
        reverse(l, left + 1, right - 1)
        temp = l[left]
        l[left] = l[right]
        l[right] = temp


def reverse01(l, left, right):
    # 循环替换递归
    while left < right:
        temp = l[left]
        l[left] = l[right]
        l[right] = temp
        left += 1
        right -= 1


if __name__ == '__main__':
    l = [56, 21, 34, 9, 12, 33, 2, 98, 16, 83]
    # reverse(l, 0, len(l) - 1)
    reverse01(l, 0, len(l) - 1)
    print(l)
