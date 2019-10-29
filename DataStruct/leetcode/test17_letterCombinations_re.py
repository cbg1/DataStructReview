# coding:utf-8
'''
1.构建9宫格键盘的字典,其中789单独处理
2.数字键组合返回所有对应的组合
3.递归回溯实现组合，next_digits长度为0则递归终止

'''


class Solution:
    def letterCombinations(self, digits: str):
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        key_dict = {}
        for i in range(2, 10):
            if i == 7:
                key_dict[str(i)] = alphas[(i - 2) * 3:(i - 2) * 3 + 4]
            elif i == 8:
                key_dict[str(i)] = alphas[(i - 2) * 3 + 1:(i - 2) * 3 + 4]
            elif i == 9:
                key_dict[str(i)] = alphas[(i - 2) * 3 + 1:(i - 2) * 3 + 5]
            else:
                key_dict[str(i)] = alphas[(i - 2) * 3:(i - 2) * 3 + 3]

        res = []

        def back_track(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in key_dict[next_digits[0]]:
                    back_track(combination + letter, next_digits[1:])

        back_track("", digits)
        return res

    def letterCombinations01(self, digits: str):
        if not digits:
            return
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        key_dict = {}
        for i in range(2, 10):
            if i == 7:
                key_dict[str(i)] = alphas[(i - 2) * 3:(i - 2) * 3 + 4]
            elif i == 8:
                key_dict[str(i)] = alphas[(i - 2) * 3 + 1:(i - 2) * 3 + 4]
            elif i == 9:
                key_dict[str(i)] = alphas[(i - 2) * 3 + 1:(i - 2) * 3 + 5]
            else:
                key_dict[str(i)] = alphas[(i - 2) * 3:(i - 2) * 3 + 3]
        # print(key_dict)
        # res每次暂存目前出的，三层for循环
        # 最外层为余下的key值，对res遍历并将以下的每个key值对应的字符串依次组合
        # 并且更新res
        res = [s for s in key_dict[digits[0]]]
        for i in digits[1:]:
            cur_res = []
            for m in res:
                for n in key_dict[i]:
                    cur_res.append(m + n)
            res = cur_res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations01("23"))
