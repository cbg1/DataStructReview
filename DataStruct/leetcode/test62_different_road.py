# coding:utf-8
import math
import numpy as np


class Solution:
    # 向右m-1步，向下n-1步就好
    def uniquePaths(self, m: int, n: int) -> int:
        # factorial阶乘函数
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    # 动态规划,空间复杂度O(m*n)
    def uniquePaths01(self, m: int, n: int) -> int:
        # 初始化矩阵，边界都为1
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(np.mat(dp).shape)
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 动态规划,空间复杂度O(2*n)
    def uniquePaths02(self, m: int, n: int) -> int:
        # 重复使用一维列表即可
        pre = [1] * n
        cur = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    # 动态规划,空间复杂度O(n)
    def uniquePaths03(self, m: int, n: int) -> int:
        # 重复使用一维列表即可
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = + cur[j - 1]
        return cur[-1]


if __name__ == '__main__':
    s = Solution()
    # counts = s.uniquePaths(3, 2)
    counts = s.uniquePaths01(3, 2)
    print(counts)
    # edges = [[0] * M for i in range(M)]
