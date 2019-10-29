# coding:utf-8
class Solution:
    '''
    先找距离最远的两根线
    再依次向内移动短的那根以获取最大面积
    '''

    def maxArea(self, height) -> int:
        # 双指针
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
