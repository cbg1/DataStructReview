# coding:utf-8
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 确定符号
        sign = (dividend > 0) ^ (divisor > 0)
        divisor = abs(divisor)
        dividend = abs(dividend)
        count = 0
        while divisor <= dividend:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1

            
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign:
            result = -result

        return min(max(result, -2 ** 31), 2 ** 31 - 1)


if __name__ == '__main__':
    dividend = 45
    divisor = -2
    s = Solution()
    print(s.divide(dividend, divisor))
