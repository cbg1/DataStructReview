# coding:utf-8
# 判断test字符是否为回文字符串
def isPalindromic(test):
    for i in range(len(test) // 2):
        if test[i] != test[len(test) - 1 - i]:
            return False
    return True

# 寻找最长回文子串
def longestPalindrome(s):
    pass

if __name__ == '__main__':
    ans = longestPalindrome("babad")
    print(ans)
