# coding:utf-8
'''二分插入排序，时间复杂度为O（n*n）'''
'''当n较大时，比较次数要远小于直接插入排序'''
'''稳定的排序算法'''


def bin_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        left, right = 0, i - 1
        # 二分查找key在已经有序的序列中的位置
        while left <= right:
            mid = (left + right) // 2
            if key < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 从右向左往后移动一位
        for j in range(i - 1, left - 1, -1):
            nums[j + 1] = nums[j]
        nums[left] = key

    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123]
    num_sorted = bin_sort(nums)
    print(num_sorted)
