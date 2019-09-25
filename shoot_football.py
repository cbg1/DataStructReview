# def shoot():
#     inputlines = input("input:")
#     res = inputlines.split(" ")
#     n = int(res[0])
#     m = int(res[1])
#     sum = 0
#     i = 2
#     j = 2 + 2 * n
#     while i < (2 * n + 2) and j < (2 + 2 * n + m):
#         print(res[i + 1], "***", res[i], "***", res[j])
#         if int(res[j]) >= int(res[i]) and int(res[j]) <= int(res[i + 1]):
#             sum += 1
#             i = 2
#             j += 1
#             if j == 2 + 2 * n + m:
#                 print(sum)
#         else:
#             i += 2
#             if i == 2 * n + 2:
#                 j += 1
#                 i = 2
#
#
# if "__main__":
#     data = "3 3 1 5 2 6 7 8 10 4 8"
#     shoot()

# # coding:utf-8
# def shoot(n, m, doors, balls):
#     i, j, score = 0, 0, 0
#     while i < n and j < m:
#         # print(doors[i][0], balls[j], doors[i][1])
#         if balls[j] >= doors[i][0] and balls[j] <= doors[i][1]:
#             score += 1
#             i = 0
#             j += 1
#             if j == m:
#                 print(score)
#         else:
#             i += 1
#             if i == n:
#                 j += 1
#                 i = 0
#
#
# if __name__ == '__main__':
#     n_m = input().strip().split(" ")
#     n, m = int(n_m[0]), int(n_m[1])
#     doors = []
#     balls = []
#     for i in range(n):
#         doors.append(list(map(int, input().strip().split(" "))))
#     for i in range(m):
#         balls.append(int(input()))
#     shoot(n, m, doors, balls)

# coding:utf-8
def shoot(n, m, doors, balls):
    i, j, score = 0, 0, 0
    for i in range(m):
        for j in range(n):
            print(doors[i][0], balls[j], doors[i][1])
            if balls[i] >= doors[j][0] and balls[i] <= doors[j][1]:
                score += 1
                break
    print(score)

if __name__ == '__main__':
    n_m = input().strip().split(" ")
    n, m = int(n_m[0]), int(n_m[1])
    doors = []
    balls = []
    for i in range(n):
        doors.append(list(map(int, input().strip().split(" "))))
    for i in range(m):
        balls.append(int(input()))
    shoot(n, m, doors, balls)
