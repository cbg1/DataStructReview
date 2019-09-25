class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s1 = ""
        if x >= 0:
            for i in range(len(s)):
                s1 = s[i] + s1
            if int(s1) > (2 ** 31 - 1):
                return 0
            else:
                return int(s1)

        else:
            for i in range(1, len(s)):
                s1 = s[i] + s1
            if -int(s1) < -2 ** 31:
                return 0
            else:
                return -int(s1)


if __name__ == '__main__':
    solution = Solution()
    x = int(input())
    print(solution.reverse(x))
