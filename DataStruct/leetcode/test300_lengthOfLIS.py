# coding:utf-8
# 最长递增子序列
class Solution:
    # 对当前元素与前面的从左到右遍历比较，计算最长子序列
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        if not nums: return 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 左边的遍历换成二分查找
    def lengthOfLIS01(self, nums) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            print("num:", num)
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            print("tails:", tails)
            if j == res:
                res += 1
        return res


if __name__ == '__main__':
    # 10,9,2,5,3,7,101,18
    nums = list(map(int, input().strip().split(",")))
    s = Solution()
    # print(s.lengthOfLIS(nums))
    print(s.lengthOfLIS01(nums))
