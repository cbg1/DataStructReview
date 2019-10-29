# coding:utf-8
from collections import defaultdict


class Solution:
    # 维护一个数组填装字串
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        sub_str = []
        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str.append(s[i])
                curr_len += 1
            else:
                sub_str = sub_str[sub_str.index(s[i]) + 1:]
                sub_str.append(s[i])
                curr_len = len(sub_str)
            max_len = max(curr_len, max_len)
        return max_len

    # 双指针,维护更新一个队列
    def lengthOfLongestSubstring01(self, s: str) -> int:
        lookup = defaultdict(int)
        max_len = 0
        start = 0
        end = 0
        counter = 0
        while end < len(s):
            # 出现重复字符
            if lookup[s[end]] > 0:
                counter += 1
            # 未出现重复字符，则向后遍历
            lookup[s[end]] += 1
            end += 1
            # 出队列
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start)
        return max_len


if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    # print(solution.lengthOfLongestSubstring(s))
    print(solution.lengthOfLongestSubstring01(s))
