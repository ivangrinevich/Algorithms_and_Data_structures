n, k = [int(i) for i in input().split()]
f = [[0 for _ in range(n)] for _ in range(n)]
f[0][0] = 1
for i in range(1, n):
    for j in range(i + 1):
        f[i][j] = 0
for i in range(n - 1):
    for j in range(i + 1):
        f[i + 1][j] = f[i + 1][j] + f[i][j]
        f[i + 1][j + 1] = f[i + 1][j + 1] + f[i][j]
if k == 0 or n == 0:
    print(1)
elif k == n:
    print(1)
else:
    if k > n / 2:
        k = n - k
    print((f[n - 1][k - 1] % 1000000007 + f[n - 1][k] % 1000000007) % 1000000007)
