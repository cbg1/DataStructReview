# -*- coding:utf-8 -*-
# 给出一个数的集合，求他们拼接起来最小的数；如{3，32，321} = 321323
# 哪个放在前面导致最小，就把哪个放在最前面
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        n = len(numbers)
        for i in range(n):
            numbers[i] = str(numbers[i])
        print(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] > numbers[j] + numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)


if __name__ == '__main__':
    nums = [3, 32, 321]
    s = Solution()
    print(s.PrintMinNumber(nums))
