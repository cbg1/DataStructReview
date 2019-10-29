class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        # 空串
        if len(s) == 0:
            return 0
        # 单个非数字字符开头
        if not s[0].isnumeric() and len(s) == 1:
            return 0
        # +-开头但是接着是非数字字符
        if (s[0] == "-" or s[0] == "+") and not s[1].isnumeric():
            return 0
        # 非+-的字符开头
        if s[0] != "+" and s[0] != "-" and not s[0].isnumeric():
            return 0

        flag = 0
        num = ""
        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                flag = 1
            for i in range(1, len(s)):
                if s[i].isnumeric():
                    num += s[i]
                else:
                    break
        else:
            for i in range(0, len(s)):
                if s[i].isnumeric():
                    num += s[i]
                else:
                    break
        if flag:
            return max(-int(num), -2 ** 31)
        else:
            return min(int(num), 2 ** 31 - 1)


if __name__ == '__main__':
    solution = Solution()
    x = input()
    print(solution.myAtoi(x))
