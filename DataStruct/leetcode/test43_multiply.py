# coding:utf-8
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addStrings(num1: str, num2: str) -> str:
            res = ""
            i, j = len(num1) - 1, len(num2) - 1
            jinwei = 0
            while i >= 0 or j >= 0:
                n1 = int(num1[i]) if i >= 0 else 0
                n2 = int(num2[j]) if j >= 0 else 0
                temp = n1 + n2 + jinwei
                jinwei = temp // 10
                res = str(temp % 10) + res
                i -= 1
                j -= 1
            if jinwei > 0:
                res = str(jinwei) + res
            return res

        res = ""
        # 竖式计算
        # 保证num1长度大于等于num2
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        n1, n2 = len(num1), len(num2)
        for j in range(n2 - 1, -1, -1):
            curr_mul = ""
            carry = 0
            for i in range(n1 - 1, -1, -1):
                temp = int(num2[j]) * int(num1[i]) + carry
                carry = temp // 10
                curr_mul = str(temp % 10) + curr_mul
            if carry > 0:
                curr_mul = str(carry) + curr_mul
            curr_mul = curr_mul + "0" * (n2 - j - 1)
            res = addStrings(res, curr_mul)
        if res == "0" * n1:
            res = "0"
        return res


if __name__ == '__main__':
    num1 = "9133"
    num2 = "0"
    s = Solution()
    print(s.multiply(num1, num2))
