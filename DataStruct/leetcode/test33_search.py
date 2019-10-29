class Solution:
    def search(self, nums, target: int) -> int:
        def rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    # Ѱ�������Ǹ���Ȼ�����ұ�һ������
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return 0

        def bin_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        min_index = rotate_index(0, n - 1)
        # ���м�
        if nums[min_index] == target:
            return min_index
        # ����������
        if min_index == 0:
            return bin_search(0, n - 1)
        # ���ұ�
        if target < nums[0]:
            return bin_search(min_index, n - 1)
        # �����
        return bin_search(0, min_index)
