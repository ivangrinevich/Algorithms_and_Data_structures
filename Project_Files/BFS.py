def bfs():
    n = int(f_input.readline())
    temp = 1
    matrix = []
    visited = [False for _ in range(n)]
    order = [0 for _ in range(n)]
    for _ in range(n):
        matrix.append([int(i) for i in f_input.readline().split()])
    for i in range(n):
        if not visited[i]:
            q = list()
            q.append(i)
            visited[i] = True
            order[i] = temp
            temp += 1
            while q:
                p = q[0]
                q.pop(0)
                for j in range(1, n):
                    if matrix[p][j] == 1 and not visited[j]:
                        visited[j] = True
                        q.append(j)
                        order[j] = temp
                        temp += 1
    print(*order, file=f_output)


with open('../Individual_task/inputs/bfs_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/bfs_output.txt', 'w', encoding='utf-8') as f_output:
    bfs()
