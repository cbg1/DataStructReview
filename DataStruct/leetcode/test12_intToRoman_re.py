# coding:utf-8
'''
先使用现有的阿拉伯数字补上要求
再将value值排序成降序
再依次从整数中拆除转化为阿拉伯数字
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        original_roman = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000}
        keys_list = list(original_roman.keys())
        values_list = list(original_roman.values())
        for i in range(0, len(original_roman) - 2, 2):
            original_roman[keys_list[i] + keys_list[i + 1]] = values_list[i + 1] - values_list[i]
            original_roman[keys_list[i] + keys_list[i + 2]] = values_list[i + 2] - values_list[i]

        original_roman = dict(sorted(original_roman.items(), key=lambda x: x[1]))

        keys_list = list(original_roman.keys())[::-1]
        values_list = list(original_roman.values())[::-1]

        res = ""
        for key, value in zip(keys_list, values_list):
            curr_freq = num // value
            for i in range(curr_freq):
                res += key
            num = num % value
        return res


if __name__ == '__main__':
    s = Solution()
    num = 1994
    print(s.intToRoman(num))
