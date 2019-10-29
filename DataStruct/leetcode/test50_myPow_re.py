# coding:utf-8
class Solution:
    # 快速幂方法
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return max(min(self.fast_pow(x, n), 2 ** 31 - 1), -2 ** 31)

    def fast_pow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 10))
