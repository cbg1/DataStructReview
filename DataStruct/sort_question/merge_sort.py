# coding:utf-8
'''序列由多个有序序列组成，归并多个有序序列即可完成排序'''
''' 时间复杂度O(nlogh2^n)，稳定算法'''


# 一次归并，相邻的长度相等的两个有序数组进行一次归并
def merge(nums, numsg, u, m, v):
    i, j, k = u, m + 1, u
    while i <= m and j <= v:
        if nums[i] <= nums[j]:
            numsg[k] = nums[i]
            i += 1
        else:
            numsg[k] = nums[j]
            j += 1
        k += 1
    # 前半段有剩余，则全部加入
    # 这里j往后移动，k往后移动了，所以不是上一个了
    if i <= m:
        for t in range(i, m + 1):
            numsg[k + t - i] = nums[t]
    # 第二段中有剩余，则全部加入
    else:
        for t in range(j, v + 1):
            numsg[k + t - j] = nums[t]


# 一趟归并
def merge_pass(nums, numsg, length):
    n = len(nums)
    i = 0
    while i <= n - 2 * length:
        merge(nums, numsg, i, i + length - 1, i + 2 * length - 1)
        i = i + 2 * length
    # 对剩余的一个长为len，另一个不足len,终点为n-1的两个有序段归并
    if (i + length - 1 < n - 1):
        merge(nums, numsg, i, i + length - 1, n - 1)
    # 对剩余长度不足len的，终点为n-1的有序段进行处理
    else:
        for j in range(i, n):
            numsg[j] = nums[j]


# 升序排序
def merge_sort(nums):
    temp = [None] * len(nums)
    length = 1
    while length < len(nums):
        merge_pass(nums, temp, length)
        length = 2 * length
        merge_pass(temp, nums, length)
        length = 2 * length
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123, 8, 12]
    print(nums)
    num_sorted = merge_sort(nums)
    print(num_sorted)
