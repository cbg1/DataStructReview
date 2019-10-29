class Solution:
    def myAtoi(self, s: str) -> int:
        # 去掉首尾的空格
        s = s.strip()
        # 不能进行有效转化则返回0
        if len(s) == 0:
            return 0
        # 不为数字的单个字符
        if not s[0].isnumeric() and len(s) == 1:
            return 0
        # 第一个字符不为+-也不为数字
        if not s[0] == "+" and not s[0] == "-" and not s[0].isnumeric():
            return 0
        # 第一个字符为+或者-，但是第二个字符不为数字
        if (s[0] == "+" or s[0] == "-") and not s[1].isnumeric():
            return 0

        if s[0] == "+" or s[0] == "-":
            sign = 0
            if s[0] == "-":
                sign = 1
            s1 = ""
            for i in range(1, len(s)):
                if s[i].isnumeric():
                    s1 += s[i]
                else:
                    break
            if sign:
                return max(-int(s1), -2 ** 31)
            else:
                return min(int(s1), 2 ** 31 - 1)
        else:
            s1 = ""
            for i in range(len(s)):
                if s[i].isnumeric():
                    s1 += s[i]
                else:
                    break

            return min(int(s1), 2 ** 31 - 1)


if __name__ == '__main__':
    solution = Solution()
    # x = input()
    print(solution.myAtoi("words and 987"))
