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


# 按中间优先左右滞后原则输出元素,非递归解决
def listorder01(nums, left, right):
    if left <= right:
        top = 0
        node = stacknode(None, None)
        stack = [node] * (len(nums))

        i, j = left, right
        # 先遍历完左边数组端，右边数组端依次入栈，
        while i <= j or top != 0:


            if i <= j:
                mid = (i + j) // 2
                print(nums[mid], end=" ")
                # print(mid + 1, j)
                stack[top].l = mid + 1
                stack[top].r = j
                top += 1
                j = mid - 1

            else:
                top -= 1
                i = stack[top].l
                j = stack[top].r

                print(len(stack))
                for s in stack:
                    print(s.l, s.r)



if __name__ == '__main__':
    nums = [18, 32, 4, 9, 26, 6, 10, 30, 12, 8, 45]
    # 6 4 18 32 9 26 12 10 30 8 45
    listorder01(nums, 0, len(nums) - 1)
