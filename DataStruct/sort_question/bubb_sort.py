# coding:utf-8
'''O(n*n)'''
'''稳定算法'''


# 升序排序
def bubb_sort(nums):
    done = 1
    for i in range(len(nums)):
        # 如果没有发生交换则直接结束
        if done:
            done = 0
            for j in range(len(nums) - i - 1):
                if nums[j + 1] < nums[j]:
                    key = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = key
                    done = 1
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123, 8, 12]
    print(nums)
    num_sorted = bubb_sort(nums)
    print(num_sorted)
