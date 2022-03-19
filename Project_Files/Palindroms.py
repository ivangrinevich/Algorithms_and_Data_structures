from array import array
with open('../Individual_task/inputs/palindroms.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/palindroms_out.txt', 'w', encoding='utf-8') as f_output:
    n = array('l')
    n.fromlist([ord(i) for i in f_input.readline().strip()])
    k = len(n)
    if n == n[::-1]:
        print(k, file=f_output)
        print(n, file=f_output)
    else:
        pal = ''
        f = [array('l', [0 for _ in range(k)]) for _ in range(k)]
        for i in range(k):
            f[i][i] = 1
        for i in range(k - 1):
            f[i][i + 1] = 2 if chr(n[i]) == chr(n[i + 1]) else 1
        for z in range(k - 2):
            j = z + 2
            for i in range(k - j):
                f[i][j] = f[i + 1][j - 1] + 2 if chr(n[i]) == chr(n[j]) else max(f[i + 1][j], f[i][j - 1])
                j += 1
        print(f[0][k - 1], file=f_output)
        i = 0
        j = k - 1
        while j >= i:
            m = f[i][j]
            while (i < k - 1) and (f[i + 1][j] == m):
                i += 1
            while j > 0 and f[i][j - 1] == m:
                j -= 1
            i += 1
            pal += chr(n[j])
            j -= 1
        print(pal + pal[::-1][f[0][k - 1] % 2:], file=f_output)

