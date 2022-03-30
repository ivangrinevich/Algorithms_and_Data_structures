n = int(input())
m = [int(i) for i in input().split()]
f = [1 for _ in range(n)]
l = set(m)
i = 0
if len(l) == 1 and l != {0}:
    print(0)
elif l == {0}:
    print(len(m) - 1)
else:
    for i in range(1, n):
        j = 0
        maximum = 0
        while j < i:
            if m[j] != 0 and m[i] % m[j] == 0:
                f[i] = f[j] + 1 if f[j] + 1 > f[i] else f[i]
                j += 1
            else:
                j += 1

    print(len(m) - max(f))
