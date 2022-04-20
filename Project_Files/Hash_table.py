with open('../Individual_task/inputs/hash_table_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/hash_table_output.txt', 'w', encoding='utf-8') as f_output:
    m, c, n = [int(i) for i in f_input.readline().split()]
    table = [-1 for _ in range(m)]
    for i in range(n):
        x = int(f_input.readline())
        for j in range(m):
            pos = (x % m + c * j) % m
            if table[pos] == -1:
                table[pos] = x
                break
            elif table[pos] == x:
                break
    print(*table, file=f_output)
