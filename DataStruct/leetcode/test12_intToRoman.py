# coding:utf-8
class Solution:
    def intToRoman(self, num: int) -> str:
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

        keys = list(original_roman.keys())[::-1]
        values = list(original_roman.values())[::-1]
        res = ""
        for key, value in zip(keys, values):
            curr_rep = num // value
            for i in range(curr_rep):
                res += key
            num = num % value
        return res



if __name__ == '__main__':
    s = Solution()
    num = 1994
    print(s.intToRoman(num))
