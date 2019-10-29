# coding:utf-8
class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        used = [False] * len(nums)
        res = []
        self._dfs(nums, 0, [], used, res)
        return res

    def _dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                #在同一层中上一个未用过
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self._dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique(nums))
