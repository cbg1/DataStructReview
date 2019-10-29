# coding:utf-8
def max_sliding_window(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n - 1]
    for i in range(1, n):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])

        j = n - i - 1
        if (j + 1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])
    res = []
    for i in range(n - k + 1):
        res.append(max(left[i + k - 1], right[i]))
    return res


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    k = int(input())
    result = max_sliding_window(nums, k)
    for max_num in result:
        print(max_num, end=" ")
