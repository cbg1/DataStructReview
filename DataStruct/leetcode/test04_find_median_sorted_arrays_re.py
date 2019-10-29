# coding:utf-8
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        # 保证n2>n1
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        # 二分法查找出m1
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = (right + left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        # 两个list合并后长度为基数，则取中间那个数
        if (n1 + n2) % 2 == 1:
            return c1
        else:
            return (c1 + c2) / 2

    '''
    1.i=0~m j=j=(m+n+1)/2-i 二分法找出符合条件的B[j - 1] < A[i]和A[i - 1] < B[j]的i值
    2.边界条件
    3.奇数和偶数个的区别
    '''

    def median(self, A, B):
        m, n = len(A), len(B)
        # 确保n大于m，这样j才会不小于0，i=0~m,j=(m+n+1)/2-i
        if m > n:
            A, B, m, n, = B, A, n, m
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        # 二分法寻找i
        while imin <= imax:
            # 找到一个符合条件的i
            i = (imin + imax) // 2
            j = half_len - i
            # i太小，必须增大
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            # i太大，必须减小
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            # i刚好满足条件
            else:
                # 寻找边界条件下的max_of_left
                # left_partA为空
                if i == 0:
                    max_of_left = B[j - 1]
                # left_partB为空
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                # 总共奇数个数
                if (m + n) % 2 == 1:
                    return max_of_left

                # 总共偶数个数
                else:
                    # 寻找边界条件下的min_of_right
                    # right_partA为空
                    if i == m:
                        min_of_right = B[j]
                    # right_partB为空
                    elif j == n:
                        min_of_right = A[i]
                    else:
                        min_of_right = min(A[i], B[j])
                    return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    # nums1 = [1, 3]
    # nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    median = s.findMedianSortedArrays(nums1, nums2)
    # median = s.median(nums1, nums2)
    print(median)
