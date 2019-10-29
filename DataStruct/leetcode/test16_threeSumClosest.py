class Solution:
    def threeSumClosest(self, nums, target):
        # 存在唯一答案
        # 先对数组进行由小到大的排序
        nums.sort()
        diff = 2 ** 31 - 1
        res = target
        for k in range(len(nums) - 1, 1, -1):
            i, j = 0, k - 1
            # 根据三数之和的大小移动ij指针
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s > target:
                    if s - target < diff:
                        diff = s - target
                        res = s
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    if target - s < diff:
                        diff = target - s
                        res = s
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

        return res


if __name__ == '__main__':
    nums = [0, 1, 2]
    target = 3
    s = Solution()
    print(s.threeSumClosest(nums, target))
