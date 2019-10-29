n = int(input())
nums = [0]
nums.extend(list(map(int, input().strip().split(" "))))

count = 0
flag = 1
curr = [0]
curr.extend([i for i in range(1, n+1)])
curr1 = curr
while flag:
    count += 1
    for i in range(1, n + 1):
        curr1[i] = nums[i]
    for j in range(1, n + 1):
        if curr[j] == curr1[j]:
            flag = 0
print(count)
