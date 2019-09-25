if __name__ == '__main__':
    n_w = input().strip().split(" ")
    n, w = int(n_w[0]), int(n_w[1])
    a = [0] * n
    b = [0] * n
    happy = [0] * n
    for i in range(n):
        ai_bi_happy = input().strip().split(" ")
        a[i], b[i], happy[i] = int(ai_bi_happy[0]), int(ai_bi_happy[1]), int(ai_bi_happy[2])
    for i in range(n):
        print(a[i], b[i], happy[i])

# 4 100
# 100 73 60
# 100 89 35
# 30 21 30
# 10 8 10
