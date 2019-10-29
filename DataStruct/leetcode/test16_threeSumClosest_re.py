# coding:utf-8
'''
数组中找到三个数最接近于target，只存在唯一答案
1.类似于上一个三数之和等于0，先对数组进行排序
2.k从右往左，i由左向右，j由k-1向左，直到ij汇合
3.ij循环去掉重复值
'''


class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        diff = 2 ** 31 - 1
        res = target
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                elif s < target:
                    i += 1
                    if target - s < diff:
                        res = s
                        diff = target - s
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                else:
                    j -= 1
                    if s - target < diff:
                        diff = s - target
                        res = s
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    target = 0
    s = Solution()
    print(s.threeSumClosest(nums, target))
