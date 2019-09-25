# coding:utf-8
''' 时间复杂度O(nlogh2^n)，不稳定算法'''


# 升序排序
def quick_sort(nums, left, right):
    if left < right:
        i = left
        j = right
        key = nums[i]
        while i < j:
            while i < j and nums[j] >= key:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= key:
                i += 1
            nums[j] = nums[i]
        nums[i] = key
        quick_sort(nums, left, i - 1)
        quick_sort(nums, i + 1, right)
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123, 8, 12]
    print(nums)
    num_sorted = quick_sort(nums, 0, len(nums) - 1)
    print(num_sorted)
