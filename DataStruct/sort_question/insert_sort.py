# coding:utf-8
'''直接插入排序，时间复杂度为O（n*n）'''
'''稳定的排序算法'''


def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        # 设置哨兵
        key = nums[i]
        # 哨兵从右往左依次与左边已经有序的子序列进行比较
        while key < nums[j] and j >= 0:
            # 子序列依次向右移动
            nums[j + 1] = nums[j]
            j = j - 1
        # 找到哨兵的位置
        nums[j + 1] = key
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123]
    num_sorted = insert_sort(nums)
    print(num_sorted)
