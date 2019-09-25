class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, step = 0, -1
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
