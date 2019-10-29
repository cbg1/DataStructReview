# coding:utf-8
class Solution:
    # # 如果p中没有*的话
    # def isMatch02(self, s: str, p: str) -> bool:
    #     if not p:
    #         return not s
    #     first_match = bool(s) and p[0] in {s[0], '.'}
    #     return first_match and self.isMatch02(s[1:], p[1:])

    # 如果p中有*的话
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == "*":
            # 前面是把a*当空看，后面是当多个任意字符
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # 动态规划
    def isMatch01(self, s: str, p: str) -> bool:
        # 自顶向下,dp(i, j)表示text[i:]和pattern[j:]是否能匹配
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:

                # 递归终止条件
                if j == len(p):
                    ans = i == len(s)
                # 继续递归
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        # 前者用掉模式 p，后者用掉text s
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                # (i,j)作为key
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    solution = Solution()
    print(solution.isMatch(s, p))
