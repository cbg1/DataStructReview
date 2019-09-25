# 3 3
# 1 2 1
# 1 2 2
# 1 2 3
if __name__ == '__main__':
    n_m = list(map(int, input().strip().split(" ")))
    n, m = n_m[0], n_m[1]
    guiman = []
    values = []
    for i in range(n):
        list1 = list(list(map(int, input().strip().split(" "))))
        a_b = [list1[0], list1[1]]
        guiman.append(a_b)
        values.append(list1[2])
    print(sum(values))
