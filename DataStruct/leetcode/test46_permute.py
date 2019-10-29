# coding:utf-8
class Solution:
    def permute(self, nums):
        def back_track(first=0):
            # 递归终止条件
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                back_track(first + 1)
                # 回溯
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        back_track()

        return res

    def permute01(self, nums):
        n = len(nums)
        if n == 0:
            return []
        used = [False] * n
        res = []
        path = []
        self._dfs(nums, path, 0, used, res)
        return res

    def _dfs(self, nums, path, index, used, res):
        # 递归终止条件
        if index == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self._dfs(nums, path, index + 1, used, res)
                print(" path1:", path, "index:", index)
                used[i] = False
                path.pop()
                print(" path2:", path, "index:", index)


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))
    print(s.permute01(nums))
