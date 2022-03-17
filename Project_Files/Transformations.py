with open('../Individual_task/inputs/transformations.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/transformations_out.txt', 'w', encoding='utf-8') as f_output:
    x = int(f_input.readline())
    y = int(f_input.readline())
    z = int(f_input.readline())
    a = list(f_input.readline().strip())
    b = list(f_input.readline().strip())
    n = len(a)
    m = len(b)
    f = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for j in range(m + 1):
        f[0][j] = j * y
    for i in range(n + 1):
        f[i][0] = i * x
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delta = 0 if a[i - 1] == b[j - 1] else 1
            f[i][j] = min(f[i - 1][j] + x, f[i][j - 1] + y, f[i - 1][j - 1] + min(z, x + y) * delta)
    print(f[n][m], file=f_output)
