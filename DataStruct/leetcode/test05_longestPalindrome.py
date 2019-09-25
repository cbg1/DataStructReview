# coding:utf-8

# 判断test是否是回文
def isPalindromic(test):
    length = len(test)
    for i in range(length // 2):
        if test[i] != test[length - i - 1]:
            return False
    return True


# 暴力解法
'''选取所有起点和终点位置的字串，判断长度和回文'''
def longestPalindrome(s):
    ans = ""
    max = 0
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            test = s[i:j]
            if isPalindromic(test) and len(test) > max:
                ans = test
                max = len(test)
    return ans


# 最长公共子串
# 将字串倒置，与原字串找最长公共子串,动态规划
def longestPalindrome1(s):
    if s == "":
        return ""
    revers = s[::-1]
    length = len(s)
    maxlen = 0
    maxend = 0
    arr = [[0] * length for i in range(length)]
    for i in range(length):
        for j in range(length):
            if s[i] == revers[j]:
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j - 1] + 1
            # 还需要添加位置判断，位置正确才是回文子串，只需要判断子串的最后一个的位置情况
            if arr[i][j] > maxlen:
                before_rev = length - j - 1
                if before_rev + arr[i][j] - 1 == i:
                    maxlen = arr[i][j]
                    maxend = i  # 以i结尾的字符
    return s[maxend - maxlen + 1: maxend + 1]


# 最长公共子串
# 将字串倒置，与原字串找最长公共子串,动态规划
# 每次只用到上一列，所以存储空间只需n所以每次更新一列
def longestPalindrome2(s):
    if s == "":
        return ""
    revers = s[::-1]
    length = len(s)
    maxlen = 0
    maxend = 0
    arr = [0] * length
    for i in range(length):
        # 倒过来以至于在用之前未被更新,也就是用的是上一列的结果
        for j in range(length - 1, -1, -1):
            if s[i] == revers[j]:
                if i == 0 or j == 0:
                    arr[j] = 1
                else:
                    arr[j] = arr[j - 1] + 1
            # 每次不用的时候置0
            else:
                arr[j] = 0
            # 还需要添加位置判断，位置正确才是回文子串，只需要判断子串的最后一个的位置情况
            if arr[j] > maxlen:
                before_rev = length - j - 1
                if before_rev + arr[j] - 1 == i:
                    maxlen = arr[j]
                    maxend = i  # 以i结尾的字符
    return s[maxend - maxlen + 1: maxend + 1]


# 扩展中心
def longestPalindrome3(s):
    if s == None or len(s) < 1:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # 以i为中心扩散
        len2 = expand_around_center(s, i, i + 1)  # 以i和i+1的空为中心扩散
        lenght = max(len1, len2)
        if lenght > (end - start):
            start = i - (lenght - 1) // 2
            end = i + lenght // 2
    return s[start:end + 1]


def expand_around_center(s, left, right):
    L = left
    R = right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


# 将字符串首端添加^,尾部添加$,字符串间隔添加#号
def preProcess(s):
    n = len(s)
    if (n == 0):
        return "^$"
    ret = "^"
    for i in range(n):
        ret += "#" + s[i]
    ret += "#$"
    return ret


# Manacher's Algorithm 马拉车算法
def longestPalindrome4(s):
    t = preProcess(s)
    n = len(t)
    p = [0] * n
    # 中心点
    c = 0
    r = 0
    for i in range(1, n - 1):
        i_mirror = 2 * c - i
        if r > i:
            p[i] = min(r - i, p[i_mirror])  # 防止超出r
        else:
            p[i] = 0  # 等于r的情况
        # 利用中心扩展方法
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if (i + p[i] > r):  # 判断是否需要更新r
            c = i
            r = i + p[i]
    # 找出最大的p值s
    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    start = (center_index - max_len) // 2
    return s[start:(start + max_len)]


if __name__ == '__main__':
    # ans = longestPalindrome("babad")
    # ans = longestPalindrome1("babad")
    # ans = longestPalindrome2("babad")
    # ans = longestPalindrome3("babad")
    ans = longestPalindrome4("babad")
    print(ans)
