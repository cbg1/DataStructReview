class Solution:
    # 暴力法超时
    def longestValidParentheses(self, s: str) -> int:
        def isValid(sub):
            if not sub or sub == "":
                return False
            stack = []
            for c in sub:
                if c == "(":
                    stack.append(c)
                else:
                    if len(stack) == 0:
                        return False
                    else:
                        stack.pop(0)
            if len(stack) == 0:
                return True
            else:
                return False

        max_len = 0
        res_str = ""
        # 遍历字符串
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isValid(s[i:j]) and (j - i) > max_len:
                    max_len = (j - i)
                    res_str = s[i:j]
        return max_len

    # 动态规划
    def longestValidParentheses01(self, s: str) -> int:
        res_max = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                # 形如()
                if s[i - 1] == "(":
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 0 + 2
                # 形如)),在前面找到一个与最后一个)对应的(
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 0 + 2
            res_max = max(res_max, dp[i])
        return res_max

    # 栈来实现
    def longestValidParentheses02(self, s: str) -> int:
        res_max = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    # 当跑空时，前面的所有的就为一个有效子串
                    stack.append(i)
                else:
                    # 此处i - stack[-1]为一个有效子串
                    res_max = max(res_max, i - stack[-1])
        return res_max

    # 两遍扫描
    def longestValidParentheses03(self, s: str) -> int:
        res_max = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res_max = max(res_max, 2 * right)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res_max = max(res_max, 2 * left)
            elif left > right:
                left = 0
                right = 0
        return res_max


if __name__ == '__main__':
    # s = "(()"
    s = "((()))()"
    solution = Solution()
    # result = solution.longestValidParentheses(s)
    # result = solution.longestValidParentheses01(s)
    # result = solution.longestValidParentheses02(s)
    result = solution.longestValidParentheses03(s)
    print(result)
