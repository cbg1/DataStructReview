# coding:utf-8

class Solution:
    '''
    暴力法，每个地方有两种情况，长度为2n的字符序列，最后出现2^2n种情况
    思路：任何时候添加括号的时候，右括号的数量不能大于左括号即可，直到添加到2n个
    1.使用递归来生成括号序列
    2.当长度等于2*n时递归终止，判断是否是合法的括号序列
    '''

    def generateParenthesis(self, n: int):
        def generate(A=[]):
            # 递归终止条件
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
            bol = 0
            for c in A:
                if c == "(":
                    bol += 1
                else:
                    bol -= 1
                if bol < 0:
                    return False
            return bol == 0

        res = []
        generate()
        return res

    '''
    回溯法，可以在放置前就判断是否合理
    1.如果当前字符累加到2*n则递归终止
    2.如果未达到则判断left是否小于n，再判断right是否小于left
    ps:依据的原理是左括号小于等于n，右括号小于等于左括号
    '''

    def generateParenthesis01(self, n: int):
        def back_track(s="", left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
            if left < n:
                back_track(s + "(", left + 1, right)
            if right < left:
                back_track(s + ")", left, right + 1)

        res = []
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
    print(s.generateParenthesis(n))
    print(s.generateParenthesis01(n))
    # print(s.generateParenthesis02(3))
