class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1
        return length

    # 双指针
    def removeElement01(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    s = Solution()
    # print(s.removeElement(nums, val))
    print(s.removeElement01(nums, val))
