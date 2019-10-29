# coding:utf-8
class Solution:
    def permute(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = []
        path = []
        index = 0
        used = [False] * n
        self._dfs(nums, path, index, used, res)
        return res

    def _dfs(self, nums, path, index, used, res):
        # 递归的终止条件
        if index == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self._dfs(nums, path, index+1, used, res)
                print("path1:",path)
                used[i] = False
                path.pop()
                print("path2:",path)


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))
