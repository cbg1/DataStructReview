# coding:utf-8
class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        path = []
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        self._dfs(candidates, 0, size, res, path, target)
        return res

    def _dfs(self, candidates, begin, size, res, path, target):
        # 递归终止条件
        if target == 0:
            res.append(path[:])
        for index in range(begin, size):
            if target < candidates[index]:
                break
            if index > begin and candidates[index] == candidates[index - 1]:
                continue
            path.append(candidates[index])
            # 由于每个元素只能取一次index + 1，不包含当前值
            self._dfs(candidates, index + 1, size, res, path, target - candidates[index])
            path.pop()


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))
