# coding:utf-8
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(n):
            if s[i] != s[n - i - 1]:
                return False
        return True
