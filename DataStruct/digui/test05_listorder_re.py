# coding:utf-8
# 按中间优先左右滞后原则输出元素,递归解决
def listorder(l, left, right):
    if left <= right:
        mid = (left + right) // 2
        print(l[mid], end=" ")
        listorder(l, left, mid - 1)
        listorder(l, mid + 1, right)


class stacknode:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    # # 按中间优先左右滞后原则输出元素,非递归解决
    # def listorder01(nums, left, right):
    #     if left <= right:
    #         top = 0
    #         stack = []
    #         i = left
    #         j = right
    #         while i <= j or top != 0:
    #             if i <= j:
    #                 mid = (i + j) // 2
    #                 print(nums[mid], end=" ")
    #                 stack.append(stacknode(mid + 1, j))
    #                 top += 1
    #                 j = mid - 1
    #             else:
    #                 top -= 1
    #                 curr_node = stack.pop()
    #                 i, j = curr_node.l, curr_node.r


# 按中间优先左右滞后原则输出元素,非递归解决
# 当取出中间数接着访问左边的数时，将右边部分的头尾压入栈，
# 当左边都访问完之后，依次取出栈顶访问
def listorder01(nums, left, right):
    if left <= right:
        top = 0
        stack = []
        i = left
        j = right
        while i <= j or top != 0:
            if i <= j:
                mid = (i + j) // 2
                print(nums[mid], end=" ")
                stack.append(stacknode(mid + 1, j))
                top += 1
                j = mid - 1
            else:
                top -= 1
                curr_node = stack.pop()
                i, j = curr_node.l, curr_node.r


if __name__ == '__main__':
    nums = [18, 32, 4, 9, 26, 6, 10, 30, 12, 8, 45]
    # 6 4 18 32 9 26 12 10 30 8 45 
    listorder(nums, 0, len(nums) - 1)
    print()
    listorder01(nums, 0, len(nums) - 1)
