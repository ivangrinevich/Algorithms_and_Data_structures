def dfs(v, m):
    visited[v] = True
    order[v] = m
    m += 1
    for j in range(n):
        if matrix[v][j] and not visited[j]:
            m = dfs(j, m)
    return m


with open('../Individual_task/inputs/dfs_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/dfs_output.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    index = 1
    visited = [False for _ in range(n)]
    order = [0 for _ in range(n)]
    matrix = [[int(i) for i in f_input.readline().split()] for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            index = dfs(i, index)
    print(*order, file=f_output)
