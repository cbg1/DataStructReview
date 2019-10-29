# coding:utf-8
# 思路：任何时候添加括号的时候，右括号的数量不能大于左括号即可，直到添加到2n个
class Solution:
    # 暴力法，每个地方有两种情况，长度为2n的字符序列，最后出现2^2n种情况
    def generateParenthesis(self, n: int):
        def generate(A=[]):
            if len(A) == 2 * n:
                if isValid(A):
                    res.append("".join(A))

            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        # 任何时候右括号的数量不能大于左括号
        def isValid(A):
            bal = 0
            for c in A:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        res = []
        generate()
        return res

    # 回溯法，可以在放置前就判断是否合理
    def generateParenthesis01(self, n: int):
        res = []

        def back_track(s="", left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                # 当前递归结束
                return
            else:
                # 左括号数量还不够n
                if left < n:
                    back_track(s + "(", left + 1, right)
                # 右括号数量小于左括号数量
                if right < left:
                    back_track(s + ")", left, right + 1)

        back_track()
        return res

    # 闭包数
    def generateParenthesis02(self, n: int):
        if n == 0:
            return [""]
        res = []
        for c in range(n):
            for left in self.generateParenthesis02(c):
                for right in self.generateParenthesis02(n - c - 1):
                    res.append("({}){}".format(left, right))
        return res


if __name__ == '__main__':
    s = Solution()
    n = 3
    # print(s.generateParenthesis(n))
    # print(s.generateParenthesis01(n))
    print(s.generateParenthesis02(3))
