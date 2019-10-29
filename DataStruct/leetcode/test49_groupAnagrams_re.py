import collections


class Solution:
    def groupAnagrams(self, strs):
        my_dict = collections.defaultdict(list)
        for c in strs:
            _s = tuple(sorted(c))
            my_dict[_s].append(c)
        return list(my_dict.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
