class Solution:
    # 一般方法
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 0:
            return 0
        i, length = 0, len(nums)
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i + 1])
                length = len(nums)
            else:
                i += 1
        return length

    # 双指针法
    def removeDuplicates01(self, nums):
        if not nums or len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                # 最后剩下的前i+1个为删完重复后的数组
                # print(nums[:i + 1])

        return i + 1


if __name__ == '__main__':
    a = [1, 1, 2]
    s = Solution()
    result = s.removeDuplicates01(a)
    print(result)
