# coding:utf-8
'''先分组，每组中记录相对较少，对组内的记录排序，再重新分组'''
'''一般比直接插入快，但是未找一个最好的缩小增量的方法'''
'''不稳定排序算法'''


def shell_sort(nums):
    d = len(nums) // 2
    # 每次组的记录个数为上一次的一般，直到每组只有一个记录为止
    while d >= 1:
        for i in range(d, len(nums)):
            key = nums[i]
            j = i - d
            # 小组内完成插入排序
            while j >= 0 and key < nums[j]:
                # 组内元素移动
                nums[j + d] = nums[j]
                j = j - d
            nums[j + d] = key

        d = d // 2
    return nums


if __name__ == '__main__':
    nums = [312, 126, 272, 226, 28, 165, 123]
    num_sorted = shell_sort(nums)
    print(num_sorted)
