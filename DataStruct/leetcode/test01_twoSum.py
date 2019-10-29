# coding:utf-8
class Solution:
    # 采用字典
    def twoSum(self, nums, target):
        my_dict = {}
        for index, num in enumerate(nums):
            # 如果是先添加则3,3  6实例不对
            if my_dict.get(target - num) is not None:
                return [my_dict.get(target - num), index]
            my_dict[num] = index

    def twoSum02(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + (i + 1)]


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
    # print(s.twoSum02(nums, target))
