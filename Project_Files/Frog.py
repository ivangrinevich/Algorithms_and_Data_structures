n = int(input())
array = [int(i) for i in input().split()]
f = [0 for _ in range(n)]
f[0] = array[0]
if n > 1:
    f[1] = -1
    jumps = []
    for i in range(2, n):
        f[i] = max(f[i - 2], f[i - 3]) + array[i]
    i = n - 1
    while i >= 0:
        if f[i] - array[i] == f[i - 2]:
            jumps.append(i + 1)
            i -= 2
        else:
            jumps.append(i + 1)
            i -= 3
    if f[n - 1] > 0:
        print(f[n - 1])
        print(*sorted(jumps))
    else:
        print(f[n - 1])
else:
    print(array[0])
    print(1)
