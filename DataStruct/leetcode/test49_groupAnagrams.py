import collections


class Solution:
    def groupAnagrams(self,strs):
        dic = collections.defaultdict(list)
        for s in strs:
            _s = ''.join(sorted(s))
            dic[_s].append(s)

        return list(dic.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
