# coding:utf-8
def three_sum_k(n, nums, k):
    if len(nums) == 0 or n <= 0:
        return 0
    nums.sort()
    res = 0
    end = n - 1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            right = end
            while j < right:
                if nums[i] + nums[j] + nums[right] < k:
                    res += right - j
                    break
                else:
                    right -= 1
    return res


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().strip().split(" ")]
    k = int(input())
    print(three_sum_k(n, nums, k))
