# coding:utf-8
'''保存中间结果，减少后面的比较次数'''
'''把数组看成以一颗树，对树进行调整'''
'''n较小时建堆调整堆反复进行,所以不提倡,时间复杂度O(nlogh2^n)，不稳定算法'''

'''
1.由k与其字节点中最小的那个比较并交换，由上往下，父子间交换
'''
# 筛选算法
# k为调整出，m为调整的下范围
def sift(nums, k, m):
    i = k
    j = 2 * i
    nums[0] = nums[k]
    finished = 0
    while j <= m and not finished:
        # 如果j+1更小的话，将j+1拿来调整
        if j < m and nums[j + 1] < nums[j]:
            j += 1
        if nums[0] <= nums[j]:
            finished = 1
        else:
            # 调整之后往下移动,从上往下调整
            nums[i] = nums[j]
            i = j
            j = 2 * j
    # 调整之后堆顶元素也得有去向
    nums[i] = nums[0]


'''
1.nums[0]留作交换时用
2.由最后一个有子节点的父节点开始往上构建小根堆
3.构建完之后，堆顶元素肯定是最小元素，将堆顶元素与最后一个交换，缩减构建堆的最后一个指标
4.最后形成的数组是降序
'''
def heap_sort(nums):
    # 从下至上对堆中所有元素构建小顶堆
    for i in range((len(nums) - 1) // 2, 0, -1):
        sift(nums, i, len(nums) - 1)

    # 构建小顶堆完毕后，取出目前树中最小元素的方法：
    # 将根节点与最后一个节点交换，堆中元素减一，再从根节点处开始调整堆
    # 最终结果是递减序列
    # i表示当前堆的大小，即等待排序元素的个数
    for i in range(len(nums) - 1, 1, -1):
        # 堆中最小的元素和最后一个元素交换，其中nums[0]作为temp
        nums[0] = nums[i]
        nums[i] = nums[1]
        nums[1] = nums[0]
        sift(nums, 1, i - 1)
    return nums


if __name__ == '__main__':
    nums = [-1, 312, 126, 272, 226, 28, 165, 123, 8, 12]
    print(nums)
    num_sorted = heap_sort(nums)
    print(num_sorted)
