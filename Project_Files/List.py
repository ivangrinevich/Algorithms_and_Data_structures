with open('../Individual_task/inputs/list_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/list_output.txt', 'w', encoding='utf-8') as f_output:
    n, m = [int(i) for i in f_input.readline().split()]
    graph = {}
    for i in range(n):
        graph[i + 1] = []
    for _ in range(m):
        u, v = [int(i) for i in f_input.readline().split()]
        graph[v].append(u)
        graph[u].append(v)
    for i in sorted(graph.keys()):
        print(len(graph[i]), *graph[i], file=f_output)
