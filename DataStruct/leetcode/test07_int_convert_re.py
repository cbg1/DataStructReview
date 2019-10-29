# coding:utf-8
# 将整数转化为字符串进行反转
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s1 = ""
        if x >= 0:
            for i in range(len(s)):
                s1 = s[i] + s1
            if int(s1) > 2 ** 31 - 1:
                return 0
            return int(s1)
        else:
            for i in range(1, len(s)):
                s1 = s[i] + s1
            if -int(s1) < -2 ** 31:
                return 0
            return -int(s1)


if __name__ == '__main__':
    solution = Solution()
    x = int(input())
    print(solution.reverse(x))
