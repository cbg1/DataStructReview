class Solution:
    def findSubstring(self, s: str, words):
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = one_word * len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            temp = s[i:i + all_len]
            c_temp = []
            # 将字符串拆成单个单词
            for j in range(0, all_len, one_word):
                c_temp.append(temp[j:j + one_word])
            print(c_temp)
            if Counter(c_temp) == words:
                res.append(i)
        return res

    # 维护一个滑动窗口计算
    def findSubstring01(self, s: str, words):
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        words_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        # 从第1,2,3，oneword-1字符开始
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            # 到最右边字符right+one_word
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    # 如果右边刚加的等于左边的，则整个区间就正好匹配
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left + one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    # 减完之后数量恰好和
                    if cur_cnt == words_num:
                        res.append(left)
        return res


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    solution = Solution()
    result = solution.findSubstring(s, words)
    print(result)
