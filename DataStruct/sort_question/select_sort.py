# coding:utf-8
'''O(n*n)'''
'''不稳定算法'''


def select_sort(nums):
    for i in range(len(nums)):
        k = i
        # 当前元素之后寻找比其小的元素
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[k]:
                k = j
        if k != i:
            key = nums[k]
            nums[k] = nums[i]
            nums[i] = key
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123]
    num_sorted = select_sort(nums)
    print(num_sorted)
