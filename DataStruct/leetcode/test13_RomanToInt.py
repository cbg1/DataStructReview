# coding:utf-8
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
        # 小数放在大数的左边或右边
        for i in range(0, len(original_roman) - 2, 2):
            original_roman[keys[i] + keys[i + 1]] = values[i + 1] - values[i]
            original_roman[keys[i] + keys[i + 2]] = values[i + 2] - values[i]

        original_roman = dict(sorted(original_roman.items(), key=lambda x: x[1]))

        keys = list(original_roman.keys())
        print(keys)

        values = list(original_roman.values())
        print(values)

        res = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                res += original_roman.get(s[i])
                i += 1
            else:
                if s[i] + s[i + 1] in keys:
                        res += original_roman.get(s[i] + s[i + 1])
                        i += 2
                else:
                    res += original_roman.get(s[i])
                    i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    roman = "IX"
    print(s.romanToInt(roman))
