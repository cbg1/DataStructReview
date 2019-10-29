class Solution:
    def extreme_insertion_index(self, nums, target, left):
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (target == nums[mid] and left):
                high = mid
            # left=falseʱ��С�ڻ����target���������ƶ��������ҵ��Ŀ϶������ұߵ�target
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target: int):
        # Ѱ������ߵ��Ǹ�����
        left_index = self.extreme_insertion_index(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.extreme_insertion_index(nums, target, False) - 1]
