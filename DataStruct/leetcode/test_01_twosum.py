# coding:utf-8
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            if num_dict.get(target - num) is not None:
                return [num_dict.get(target - num), i]
            num_dict[num] = i


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(" ")))
    target = int(input())
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)
