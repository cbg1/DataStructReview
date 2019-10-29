class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 下一个全排列
        first_index = -1
        length = len(nums)

        def reverse(nums, left, right):
            i = left
            j = right
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 从右向左找出第一对逆序数，也就是左边小于右边的数
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break
        # 无，说明数为逆序
        if first_index == -1:
            reverse(nums, 0, length - 1)
            return
        else:
            second_index = -1
            # 从右向左找到第一个大于first_index的数
            for j in range(length - 1, first_index, -1):
                if nums[j] > nums[first_index]:
                    second_index = j
                    break
        nums[second_index], nums[first_index] = nums[first_index], nums[second_index]
        reverse(nums, first_index + 1, length - 1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    s.nextPermutation(nums)
    print(nums)
