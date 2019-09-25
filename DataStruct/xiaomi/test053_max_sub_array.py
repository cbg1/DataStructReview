# coding:utf-8

class Solution:
    def max_sub_array(self, nums):
        ans = nums[0]
        sum = 0
        n = len(nums)
        for i in range(n):
            if sum + nums[i] > nums[i]:
                sum += nums[i]
            else:
                sum = nums[i]
            ans = max(ans, sum)
        return ans


if __name__ == '__main__':
    arr = list(map(int, input().strip().split(",")))
    s = Solution()
    result = s.max_sub_array(arr)
    print(result)
