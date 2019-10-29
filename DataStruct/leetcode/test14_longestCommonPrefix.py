class Solution:
    def longestCommonPrefix(self, strs: object) -> object:
        if len(strs) <= 0:
            return ""
        length = min([len(s) for s in strs])
        i = 0
        flag = True
        pre = ""
        while i < length and flag:
            curr = pre + strs[0][i]
            for s in strs:
                if not s.startswith(curr):
                    flag = False
            if flag:
                pre = curr
            i += 1
        return pre


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
