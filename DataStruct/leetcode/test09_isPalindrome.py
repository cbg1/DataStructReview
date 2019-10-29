# coding:utf-8
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = True
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x) - 1 - i]:
                res = False
        return res
