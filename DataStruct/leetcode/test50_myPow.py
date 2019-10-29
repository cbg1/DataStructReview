class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        for i in range(n):
            res = res * x
        return max(min(res, 2 ** 31 - 1), -2 ** 31)

    def fast_pow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow01(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = self.fast_pow(x, n)
        return max(min(res, 2 ** 31 - 1), -2 ** 31)


if __name__ == '__main__':
    s = Solution()
    # print(s.myPow(2, 10))
    print(s.myPow01(2, 10))
