class Solution:
    def threeSum(self, nums):
        res = []
        # 先对数组进行由小到大的排序
        nums.sort()
        for k in range(len(nums) - 1, 1, -1):
            if nums[k] < 0:
                break
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                continue
            i, j = 0, k - 1
            # 根据三数之和的大小移动ij指针
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
