n_m = list(map(int, input().strip().split(" ")))
n, m = n_m[0], n_m[1]
str_list = []
for _ in range(n):
    str_list.append(input())
str_list = str_list[::-1]
str_list1, str_list2 = [], []
for _ in range(m):
    str1_str2 = list(input().strip().split(" "))
    str_list1.append(str1_str2[0])
    str_list2.append(str1_str2[1])

for i in range(m):
    if str_list1[i].startswith(str_list2[i]):
        print("-1")
    elif str_list2[i].startswith(str_list1[i]):
        flag = 0
        bijiao = []
        for j in range(n):
            if str_list[j].startswith(str_list1[i]) and not str_list[j].startswith(str_list2[i]) and len(
                    str_list[j]) >= len(str_list2[i]):
                bijiao.append(str_list[j])
                flag = 1
        if flag == 0:
            print("-1")
        else:
            result = ""
            min_len = 300000
            for s in bijiao:
                if len(s) < min_len:
                    result = s
                    min_len = len(s)
            print(result)
    else:
        flag = 0
        bijiao = []
        for j in range(n):
            if str_list[j].startswith(str_list1[i]) and len(str_list[j]) >= max(len(str_list1[i]),
                                                                                len(str_list2[i])):
                bijiao.append(str_list[j])
                flag = 1
        if flag == 0:
            print("-1")
        else:
            result = ""
            min_len = 300000
            for s in bijiao:
                if len(s) < min_len:
                    result = s
                    min_len = len(s)
            print(result)
