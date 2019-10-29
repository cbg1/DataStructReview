# coding:utf-8
class Solution:
    def searchInsert(self, nums, target: int):
        n = len(nums)
        left = 0
        right = n - 1
        # 返回大于等于target的第一个索引则用left，否则用right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 如果写两个分支
    def searchInsert01(self, nums, target: int):
        size = len(nums)
        if size == 0:
            return 0
        left = 0
        right = size
        while left < right:
            mid = left + (right - left) // 2
            # 此处中位数小于目标值则排除掉，否则得包含中位数
            if nums[mid] < target:
                left = mid + 1
            else:  # >=
                right = mid
        return left

    # 如果写两个分支
    # 范围为[0,size-1]
    def searchInsert02(self, nums, target: int):
        size = len(nums)
        if size == 0:
            return 0
        if nums[-1] < target:
            return size
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:  # >=
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    s = Solution()
    # print(s.searchInsert(nums, target))
    print(s.searchInsert01(nums, target))
