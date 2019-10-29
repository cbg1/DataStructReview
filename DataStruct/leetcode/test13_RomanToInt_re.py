# coding:utf-8
'''
先将字典补全
再判断当前是否为最后一个，如果为最后一个，则只考虑是否存在在字典中
否则，
    则判断连续连个字符是否出现在字典中
    如果连续两个未出现在字典中则判断单字符即可

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        original_roman = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000}
        keys = list(original_roman.keys())
        values = list(original_roman.values())

        for i in range(0, len(original_roman) - 2, 2):
            original_roman[keys[i] + keys[i + 1]] = values[i + 1] - values[i]
            original_roman[keys[i] + keys[i + 2]] = values[i + 2] - values[i]
        res = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                res += original_roman.get(s[i])
                i += 1
            else:
                if s[i] + s[i + 1] in original_roman.keys():
                    res += original_roman.get(s[i] + s[i + 1])
                    i += 2
                else:
                    res += original_roman.get(s[i])
                    i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    roman = "MCMXCIV"
    print(s.romanToInt(roman))
