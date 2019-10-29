# coding:utf-8
'''
1.寻找数组中最短字符的长度，作为基准
2.以第一个为匹配目标,依次匹配数组中的字符串
3.注意匹配成功和失败后对前缀的影响

'''


class Solution:
    def longestCommonPrefix(self, strs) -> object:
        if len(strs) <= 0:
            return ""
        min_len = min([len(s) for s in strs])
        res = ""
        i = 0
        flag = True
        while i < min_len and flag:
            curr_pre = res + strs[0][i]
            for s in strs:
                if not s.startswith(curr_pre):
                    flag = False
            if flag:
                res = curr_pre
            i += 1
        return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
