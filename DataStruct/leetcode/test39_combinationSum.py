# coding:utf-8
class Solution:
    def combinationSum(self, candidates, target: int):
        size = len(candidates)
        if size == 0:
            return []
        res = []
        path = []
        self._dfs(candidates, 0, size, path, res, target)
        return res

    def _dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            res.append(path[:])

        # 后面比前面大，也就是更深层边比浅层大或等于，这样就不会有重复结果
        for index in range(begin, size):
            if target < 0:
                break
            path.append(candidates[index])
            #从index开始，包含当前值，可以多次取数
            self._dfs(candidates, index, size, path, res, target - candidates[index])
            # pop掉栈顶元素进行下一步计算
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))
