# coding:utf-8
# 逆序数没有下一个

class Solution:

    def nextPermutation(self, nums) -> None:

        # 从右边开始向左找到第一对nums[k]<nums[k+1],若不存在则是逆序数，直接翻转
        # 再从右边向左找到num[l]>nums[k]的l
        # 交换nums[l]和nums[k]
        # 最后翻转nums[k:]
        n = len(nums)
        first_index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break
        # 是逆序数，不存在下一个
        if first_index == -1:
            reverse(nums, 0, n - 1)
            return
        # 在first_index右边从右至左寻找第一个大于nums[first_index]的数
        second_index = -1
        for i in range(n - 1, first_index, -1):
            if nums[i] > nums[first_index]:
                second_index = i
                break
        # 替换之后，first_index右边任然是逆序，因此需要对右边的进行翻转，即为当前的下一个
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(nums, first_index + 1, n - 1)
        return nums


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    s = Solution()
    nums = list(map(int, input().strip().split(" ")))
    print(nums)
    nums = s.nextPermutation(nums)
    print(nums)
