def remove_two(list_):
    list_.sort()
    i, j = 0, len(list_) - 1
    while i < j:
        if list_[i] == list_[j]:
            break
        i += 1
        j -= 1
    if i > j:
        return "YES"
    else:
        return "NO"


def remove_two01(list_, n):
    counts = [0] * n
    for i in range(len(list_)):
        counts[list_[i] - 1] += 1
    count = 0
    flag = False
    for j in counts:
        count += j
        if count == n // 2:
            flag = True
    if flag:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        list_ = list(map(int, input().split()))
        result = remove_two01(list_, n)
        print(result)
