# coding:utf-8
'''
1.定义一个大小为numRows元素为字符串的数组
2.步伐初始化为-1，当遇到i == 0 or i == numRows - 1边界情况时步子的符号
也就是掉头计算
3.最后用完原字符后合并数组即可
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, step = 0, -1
        res = [""] * numRows
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                step = -step
            i += step
        return "".join(res)


if __name__ == '__main__':
    solution = Solution()
    s = "LEETCODEISHIRING"
    result = solution.convert(s, 3)
    print(result)
