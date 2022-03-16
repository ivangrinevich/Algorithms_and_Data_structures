with open('../Individual_task/inputs/palindroms.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/palindroms_out.txt', 'w', encoding='utf-8') as f_output:
    n = f_input.readline().strip()
    k = len(n)
    f = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        f[i][i] = 1
    for i in range(k - 1):
        f[i][i + 1] = 2 if n[i] == n[i + 1] else 1
    for j in range(2, k):
        for i in range(k - j):
            f[i][i + j] = f[i + 1][i + j - 1] + 2 if n[i] == n[i + j] else max(f[i + 1][i + j], f[i][i + j - 1])
    i = 0
    j = k - 1
    sb = ''
    while j >= i:
        m = f[i][j]
        while (i < k - 1) and (f[i + 1][j] == m):
            i += 1
        while j > 0 and f[i][j - 1] == m:
            j -= 1
        i += 1
        sb += (n[j])
        j -= 1
    print(str(f[0][k - 1]), file=f_output)
    print(sb + sb[::-1][f[0][k - 1] % 2:], file=f_output)
