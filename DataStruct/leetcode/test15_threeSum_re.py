# coding:utf-8
'''
1.先对数组进行排序
2.设置三个指针，i,j,k,满足为nums[i]+nums[j]+nums[k]=0
3.ij为左右指针，k为由右往左遍历,nums[k]如果为小于0则结束循环
4.k碰到与上一个重复值则continue
ps ij指针的变动的条件时i<j，不需要考虑i==0和j==k-1的情况，因为+1或者-1后的操作
'''


class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            if nums[k] < 0:
                break
            if k < n - 1 and nums[k] == nums[k + 1]:
                continue
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
