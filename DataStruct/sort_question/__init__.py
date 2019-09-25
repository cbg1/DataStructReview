# 基数排序
# 输入：待排序数组s, keysize关键字位数, 亦即装箱次数, radix基数
def RadixSort(s, keysize=4, radix=10):
    # 按关键字的第k分量进行分配 k = 4,3,2,1
    def distribute(s, k):
        box = {r: [] for r in range(radix)}  # 分配用的空箱子
        for item in s:  # 依次扫描s[]，将其装箱
            t = item
            t /= 10 ** (k - 1)
            t %= 10  # 去关键字第k位
            box[t].append(item)
        return box

    # 按分配结果重新排列数据
    def collect(s, box):
        a = 0
        for i in range(radix):
            s[a:a + len(box[i])] = box[i][:]  # 将箱子中元素的合并，覆盖到原来的数组中
            a += len(box[i])  # 增加偏移值

    # 核心算法

    for k in range(1, keysize + 1):
        box = distribute(s, k)  # 按基数分配
        collect(s, box)  # 按分配结果拼合
if __name__ == '__main__':
    nums = [312, 126, 272, 226, 8, 165, 123, 12, 28]
    RadixSort(nums)
    print(nums)
