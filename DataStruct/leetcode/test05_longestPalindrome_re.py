# coding:utf-8

# 判断test是否是回文
def isPalindromic(test):
    n = len(test)
    for i in range(n // 2):
        if test[i] != test[n - 1 - i]:
            return False
    return True


# 暴力解法
# 选取所有起点和终点位置的字串，判断长度和回文
def longestPalindrome(s):
    res = ""
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            test = s[i:j]
            if isPalindromic(test) and len(test) > max_len:
                res = s[i:j]
                max_len = len(test)
    return res


# 最长公共子串
# 将字串倒置，与原字串找最长公共子串,动态规划
def longestPalindrome1(s):
    # 字符串与倒置后的字符串求最大公共字串，然后判断是否为回文串
    # 不为矩阵边缘则有arr[i][j] = arr[i - 1][j - 1] + 1
    if s == "":
        return ""
    reversed_s = s[::-1]
    max_len = 0
    max_end = 0
    n = len(s)
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i] == reversed_s[j]:
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    # 连续字串的递推式
                    arr[i][j] = arr[i - 1][j - 1] + 1
            # 还需要添加位置判断，位置正确才是回文子串，只需要判断子串的最后一个的位置情况
            if arr[i][j] > max_len:
                # 获取到j倒置前的坐标
                before_reverse = n - j - 1
                # 当前j的字符也包含在字串内，所以有减一
                if (before_reverse + arr[i][j] - 1) == i:
                    max_len = arr[i][j]
                    max_end = i
    return s[max_end - max_len + 1:max_end + 1]


# 最长公共子串
# 将字串倒置，与原字串找最长公共子串,动态规划
# 每次只用到上一列，所以存储空间只需n所以每次更新一列
def longestPalindrome2(s):
    # 字符串与倒置后的字符串求最大公共字串，然后判断是否为回文串
    # 不为矩阵边缘则有arr[i][j] = arr[i - 1][j - 1] + 1
    if s == "":
        return ""
    max_len = 0
    max_end = 0
    n = len(s)
    reversed_s = s[::-1]
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # arr = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if s[i] == reversed_s[j]:
    #             if i == 0 or j == 0:
    #                 arr[i][j] = 1
    #             else:
    #                 arr[i][j] = arr[i - 1][j - 1] + 1
    #         if arr[i][j] > max_len:
    #             before_reversed = n - j - 1
    #             # 根据j来推断倒置前的位置
    #             # 将之前的位置加上字串长-1的得到字串的尾部，如果等于i则为回文子串
    #             if (before_reversed + arr[i][j] - 1) == i:
    #                 max_len = arr[i][j]
    #                 max_end = i
    # return s[max_end - max_len + 1:max_end + 1]
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    arr = [0] * n
    # i表示上一列的信息
    for i in range(n):
        # 如果从前往后更新的话，则arr[8]=a[7]+1时，a[7]不是前面的，是更新之后的
        for j in range(n - 1, -1, -1):
            if s[i] == reversed_s[j]:
                if i == 0 or j == 0:
                    arr[j] = 1
                else:
                    arr[j] = arr[j - 1] + 1
            else:
                arr[j] = 0

            if arr[j] > max_len:
                before_reversed = n - j - 1
                if (before_reversed + arr[j] - 1) == i:
                    max_len = arr[j]
                    max_end = i
    return s[max_end - max_len + 1:max_end + 1]


'''暴力解法的优化
1.外层循环为子串长度，内层为子串起始位置，如果end超出则跳出内存循环
2.p表示起始位置和结束位置的子串是否回文
3.根据p[i][j]=p[i+1][j-1] and s[i]==s[j]跌代更新，子串长度为1或2时单独计算
4.更新完之后寻找最大回文子串
'''


def longestPalindrome5(s):
    max_len = 0
    max_pal = ""
    n = len(s)
    p = [[False] * n for _ in range(n)]
    # 先求出来长度短的，后可以扩充求长度长的
    for curr_len in range(1, n + 1):
        for start in range(n):
            end = start + curr_len - 1
            if end >= n:
                break
            if curr_len == 1:
                p[start][end] = s[start] == s[end]
            elif curr_len == 2:
                p[start][end] = s[start] == s[end]
            else:
                p[start][end] = p[start + 1][end - 1] and s[start] == s[end]
            if p[start][end] and curr_len > max_len:
                max_pal = s[start:end + 1]
    return max_pal


'''暴力解法的优化,使用一维空间'''


# 为了优化空间，采用另一种循环方式

def longestPalindrome6(s):
    n = len(s)
    res = ""
    dp = [[False] * n for _ in range(n)]
    # 先有i+1和j-1才有ij，所以i倒序，j正序
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # 子串长度小于等于2
            if j - i < 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            if dp[i][j] and (j - i + 1) > len(res):
                res = s[i:j + 1]
    return res


# longestPalindrome6的优化空间
def longestPalindrome7(s):
    n = len(s)
    res = ""
    p = [False] * n
    # 先有i+1和j-1才有ij，所以i倒序，j为什么是倒序?
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i - 1, -1):
            # 子串长度小于等于3
            print(j, p[j - 1])
            if j - i < 3:
                p[j] = s[i] == s[j]
            else:
                p[j] = p[j - 1] and s[i] == s[j]
            if p[j] and (j - i + 1) > len(res):
                res = s[i:j + 1]
    return res


# 扩展中心
# 根据字符奇数偶数长，可有n+n-1个中心
def longestPalindrome3(s):
    if s == None or len(s) < 1:
        return ""
    start, end = 0, 0
    for i in range(0, len(s)):
        # 单个字符开始扩展
        len1 = expand_around_center(s, i, i)
        # 两个字符开始扩展
        len2 = expand_around_center(s, i, i + 1)
        len_max = max(len1, len2)
        if len_max > end - start:
            start = i - (len_max - 1) // 2
            end = i + len_max // 2
    return s[start:end + 1]


# 根据当前子串向左右各扩一个字符
def expand_around_center(s, left, right):
    L, R = left, right
    # 此处的R=n时已经被排除了
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1


# 解决奇数偶数问题，在中间插入#
# 将字符串首端添加^,尾部添加$,字符串间隔添加#号
def preProcess(s):
    n = len(s)
    if n == 0:
        return "^$"
    res = "^"
    for i in range(n):
        res += "#" + s[i]
    res += "#$"
    return res


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

        # 判断是否需要更新r
        if (i + p[i] > r):
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
    # ans = longestPalindrome2("a")
    # ans = longestPalindrome5("babad")
    # ans = longestPalindrome6("babad")
    # ans = longestPalindrome7("babad")
    # ans = longestPalindrome3("babad")
    ans = longestPalindrome4("babad")
    print(ans)
