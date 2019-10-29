# coding:utf-8
# 遍历找到最高点
# 初始化容量数组，cap[i] = max - h[i] 假设都有水
# 从两边往中间扫，记录一个当前最大值 lim, cap[i] = lim - h[i] 比最大值高的水都流走了
# 对 cap 数组求和即可
class Solution:
    def trap(self, height) -> int:
        max_num = 0
        max_index = 0
        n = len(height)
        for i in range(n):
            if height[i] > max_num:
                max_num = height[i]
                max_index = i

        cap = [0] * n
        for i in range(n):
            cap[i] = max_num - height[i]

        # 从左边向右扫描
        lim = 0
        for i in range(max_index):
            if height[i] > lim:
                # lim给后面的小于他的才能关水用
                lim = height[i]
                cap[i] = 0
            else:
                # 如果不大于lim则lim-当前高则为关水
                cap[i] = lim - height[i]

        # 从右边向左扫描
        lim = 0
        for i in range(n - 1, max_index, -1):
            if height[i] > lim:
                lim = height[i]
                cap[i] = 0
            else:
                cap[i] = lim - height[i]
        print(cap)
        return sum(cap)


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
