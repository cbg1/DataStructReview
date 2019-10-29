# coding:utf-8
n_m = list(map(int, input().strip().split(" ")))
n, m = n_m[0], n_m[1]
nums = list(map(int, input().strip().split(" ")))
max_mean = 0
mat = [[0] * n for i in range(n)]
for i in range(n - m + 1):
    curr_mean = sum(nums[i:i + m]) / m
    for j in range(i):
        if mat[j][i + m] != 0:
            mean = mat[j][i + m]
        else:
            mean = sum(nums[j:i + m]) / (i + m - j)
            mat[j][i + m] = mean
        if mean > curr_mean:
            curr_mean = mean

    for k in range(i + m, n - 1):
        if sum(nums[i:k]) / (k - i) > mean:
            if mat[i][k] != 0:
                mean = mat[i][k]
            else:
                mean = sum(nums[i:k]) / (k - i)
                mat[i][k] = mean

    if mean > max_mean:
        max_mean = mean
print("{0:.3f}".format(max_mean))

# n = int(input())
# nums = []
# for i in range(n):
#     num_input = list(map(int, input().strip().split(" ")))
#     a, t = num_input[0], num_input[1]
#     nums.append([a, t])
# nums.sort()
# nums[::] = nums[::-1]
# v0 = 0
# L = 0
# for a_t in nums:
#     L += v0 * a_t[1] + 0.5 * a_t[0] * a_t[1] ** 2
#     v0 = v0 + a_t[0] * a_t[1]
# print(round(L, 1))

# coding:utf-8
n_m = list(map(int, input().strip().split(" ")))
n, m = n_m[0], n_m[1]
nums = list(map(int, input().strip().split(" ")))
max_mean = 0
for i in range(n - m + 1):
    mean = sum(nums[i:i + m]) / m
    for j in range(i):
        if sum(nums[j:i + m]) / (i + m - j) > mean:
            mean = sum(nums[j:i + m]) / (i + m - j)
    for k in range(i + m, n - 1):
        if sum(nums[i:k]) / (k - i) > mean:
            mean = sum(nums[i:k]) / (k - i)

    if mean > max_mean:
        max_mean = mean
print("{0:.3f}".format(max_mean))
