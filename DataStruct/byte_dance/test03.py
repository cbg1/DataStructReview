# coding:utf-8
def max_score(n, nums):
    dp_fir = [[0] * n for _ in range(n)]
    dp_sec = [[0] * n for _ in range(n)]
    for i in range(n):
        dp_fir[i][i] = nums[i]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            left = nums[i] + dp_sec[i + 1][j]
            right = nums[j] + dp_sec[i][j - 1]
            if left > right:
                dp_fir[i][j] = left
                dp_sec[i][j] = dp_fir[i + 1][j]
            else:
                dp_fir[i][j] = right
                dp_sec[i][j] = dp_fir[i][j - 1]
    return dp_fir[0][n - 1]


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    result = max_score(n, nums)
    print(result)
