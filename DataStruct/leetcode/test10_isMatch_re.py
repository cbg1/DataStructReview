# coding:utf-8
class Solution:
    # # 如果p中没有*的话
    def isMatch02(self, s: str, p: str) -> bool:
        # 判断p是否为空串，如果p为空串，s也为空串，则返回True
        if not p:
            return not s
        # 如果s为空串则不执行and后面的逻辑
        first_match = bool(s) and p[0] in {s[0], "."}
        return first_match and self.isMatch02(s[1:], p[1:])

    # 回溯法
    # 先判断p和s为空的情况，
    # 如果模式中有星号，则出现在第二个位置，则删除匹配串中第一个等于模式的当前字符
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], "."}
        if len(p) >= 2 and p[1] == "*":
            # 模式串中的a*出现0次 或者 a*出现多次
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # 动态规划
    def isMatch01(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                # 递归终止条件
                if j == len(p):
                    ans = i == len(s)
                else:
                    pass
            return memo[i, j]


if __name__ == '__main__':
    s = ""
    p = "."
    print(bool(s))
    solution = Solution()
    print(solution.isMatch02(s, p))
