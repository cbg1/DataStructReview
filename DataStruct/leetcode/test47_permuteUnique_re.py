# coding:utf-8
class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = []
        path = []
        used = [False] * n
        index = 0
        self._dfs(nums, index, path, used, res)
        return res

    def _dfs(self, nums, index, path, used, res):
        if index == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                self._dfs(nums, index + 1, path, used, res)
                used[i] = False
                path.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique(nums))
