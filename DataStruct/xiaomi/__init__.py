# coding=utf-8
import sys


def max_continue_sum(nums):
    length = len(nums)
    tmp = nums[0]
    res = tmp
    for i in range(1, length):
        if tmp + nums[i] > nums[i]:
            tmp += nums[i]
            res = max(tmp, res)
        else:
            tmp = nums[i]
            res = max(res, tmp)
    return res


if __name__ == "__main__":
    nums = list(map(int, input().strip().split(" ")))
    result = max_continue_sum(nums)
    print(result)
