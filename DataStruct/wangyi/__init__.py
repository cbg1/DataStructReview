n = int(input())
nums = list(map(int, input().strip().split(" ")))
sum = 0
for i in range(n):
    t = nums[i]
    for j in range(i, n):
        if t > nums[j]:
            sum += j - i
print(sum)
