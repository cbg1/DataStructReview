n_k = list(map(int, input().strip().split(" ")))
n, k = n_k[0], n_k[1]
if n <= 0 or k <= 0:
    print(0)
c = []
a, b = [], []
for _ in range(n):
    a_b = list(map(int, input().strip().split(" ")))
    a.append(a_b[0])
    b.append(a_b[1])
for i in range(n):
    c.append(a[i] * b[i])
c_index = [i[0] for i in sorted(enumerate(c), key=lambda x: x[1])]
c_k_index = c_index[-k:]
a_k, b_k = [], []
for i in c_k_index:
    a_k.append(a[i])
    b_k.append(b[i])
print(sum(a_k) * min(b_k))
