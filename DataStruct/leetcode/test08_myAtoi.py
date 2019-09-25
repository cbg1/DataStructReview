class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s[0].isnumeric():
            return 0
        neg = 0
        num = ""
        if s[0] == "+" or s[0] == "-":
            if s[0] == "+":
                neg = 1

            for i in range(1, len(s)):
                if s[i].isnumeric():
                    num += s[i]
        else:
            num = ""
            for i in range(len(s)):
                if s[i].isnumeric():
                    num += s[i]
        if neg:
            return max(-2 ** 31, -int(num))
        else:
            return min(2 ** 31 - 1, int(num))


if __name__ == '__main__':
    solution = Solution()
    x = input()
    print(solution.myAtoi(x))
