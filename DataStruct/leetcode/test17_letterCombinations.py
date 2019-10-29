# coding:utf-8
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
        # print(key_dict)

        res = []

        # 递归实现回溯
        def back_track(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in key_dict[next_digits[0]]:
                    back_track(combination + letter, next_digits[1:])

        if digits:
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
        res = [i for i in key_dict[digits[0]]]
        for i in digits[1:]:
            res1 = []
            for m in res:
                for n in key_dict[i]:
                    res1.append(m + n)
            res = res1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations01("23"))
