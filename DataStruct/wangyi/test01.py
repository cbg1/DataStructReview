t = int(input())
all_list = []
for i in range(t):
    all_list.append(list(map(int, input().strip().split(" "))))
for i in range(t):
    curr_list = all_list[i]
    max_num = max(curr_list)
    curr_list.remove(max_num)
    if max_num > 2 * sum(curr_list):
        yu = max_num % 2
        if yu == 0:
            print(max_num // 2)
        else:
            print(max_num // 2 + 1)
    else:
        curr_list.append(max_num)
        yushu = (curr_list[0] + curr_list[1] + curr_list[2]) % 3
        mean = (curr_list[0] + curr_list[1] + curr_list[2]) // 3
        if yushu == 0:
            print(mean)
        elif yushu == 1:
            print(mean + 1)
        elif yushu == 2:
            print(mean + 2)
