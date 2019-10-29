class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = (right - left) * min(height[right], height[left])
        while left < right:
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

            curr_area = (right - left) * min(height[right], height[left])
            if curr_area > max_area:
                max_area = curr_area
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
