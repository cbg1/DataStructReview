# # coding:utf-8
# n_m = list(map(int, input().strip().split(" ")))
# n, m = n_m[0], n_m[1]
# a = list(map(int, input().strip().split(" ")))
#
#
# def is_not_down(a):
#     res = True
#     for i in range(len(a) - 1):
#         for j in range(i + 1, len(a)):
#             if a[i] > a[j]:
#                 res = False
#     return res
#
#
# if n <= 0:
#     print(0)
# count = 0
# while not is_not_down(a):
#     for i in range(len(a)):
#         a[i] = (a[i] + 1) % m
#         count += 1
# print(count)
# # 5 7
# # 0 1 1 4 6

def leastCount():
    lines = input().split(" ")
    n = int(lines[0])
    m = int(lines[1])
    numbers = [int(x) for x in input().split(" ")]
    max_num = 0
    cur_num = 0
    for i in range(n - 1):
        if numbers[i] <= numbers[i + 1]:
            cur_num += 1
        else:
            cur_num += 2
            if cur_num >= max_num:
                max_num = cur_num
    print(max_num)


if __name__ == '__main__':
    leastCount()
