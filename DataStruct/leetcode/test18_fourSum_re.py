# coding:utf-8

'''
数组中寻找四个数的和为target
参照三数之和
1.先对数组进行排序
2.先固定两个数再采用双指针寻找其他两个元素
3.避免重复值的情况
'''


class Solution:
    # 参照三数之和
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        if n == 0:
            return []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                left = j + 1
                right = n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif s > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))
