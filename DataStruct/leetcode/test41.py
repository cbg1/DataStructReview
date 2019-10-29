# coding:utf-8
# 检查 1 是否存在于数组中。如果没有，则已经完成，1 即为答案。
# 如果 nums = [1]，答案即为 2 。
# 将负数，零，和大于 n 的数替换为 1 。
# 遍历数组。当读到数字 a 时，替换第 a 个元素的符号。
# 注意重复元素：只能改变一次符号。由于没有下标 n ，使用下标 0 的元素保存是否存在数字 n。
# 再次遍历数组。返回第一个正数元素的下标。
# 如果 nums[0] > 0，则返回 n 。
# 如果之前的步骤中没有发现 nums 中有正数元素，则返回n + 1。
class Solution:
    def firstMissingPositive(self, nums) -> int:
        if 1 not in nums:
            return 1
        if nums == [1]:
            return 2
        n = len(nums)
        # 缺失正数一定小于等于n+1，n单独考虑
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        #读取到a替换num[a]符号，重复只改变一次，因为表示存在
        #没有num[n],所以遇到n则改写num[0]
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        print(nums)
        #先判断1~n-1，最后但前面都出现了，再判断n，由小到大原则
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1


if __name__ == '__main__':
    # nums = [1, 2, 0]
    nums = [3,4,-1,1]
    s = Solution()
    print(s.firstMissingPositive(nums))
