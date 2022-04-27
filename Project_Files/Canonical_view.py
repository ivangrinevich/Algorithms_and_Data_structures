with open('../Individual_task/inputs/canonical_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/canonical_output.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    graph = {}
    for i in range(n):
        graph[i + 1] = 0
    for _ in range(n - 1):
        u, v = [int(i) for i in f_input.readline().split()]
        graph[v] = u
    for i in sorted(graph.keys()):
        print(graph[i], end=' ', file=f_output)
