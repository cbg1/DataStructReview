class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
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


if __name__ == '__main__':
    num1 = "51189"
    num2 = "967895"
    s = Solution()
    print(s.addStrings(num1, num2))
