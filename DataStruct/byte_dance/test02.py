N = int(input())
time = []
res = []
for i in range(N):
    x, y = list(map(int, input().split()))
    time.append(x)
    res.append(y)
temp = 0
ans = 0
ans_time = 0
for i in range(1, len(time)):
    xx = time[i] - time[i - 1]
    if res[i - 1] - xx > 0:
        temp = res[i] + (res[i - 1] - xx)
    else:
        temp = res[i]
    res[i] = temp
    if ans < temp:
        ans = temp
ans_time = len(time) + temp
print(ans_time, ans)
