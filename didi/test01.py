# coding:utf-8
# 5 2
# 1 4
# 3 4
if __name__ == '__main__':
    n_m = list(map(int, input().strip().split(" ")))
    n, m = n_m[0], n_m[1]
    yuesu = []
    for i in range(m):
        yuesu.append(list(sorted(list(map(int, input().strip().split(" "))))))
    count = 0
    for i in range(m):
        current = yuesu[i][0]
        for j in range(m):
            if yuesu[j][0] == current and list([yuesu[i][1], yuesu[j][1]]) in yuesu:
                count += 1
    print(n - count)
