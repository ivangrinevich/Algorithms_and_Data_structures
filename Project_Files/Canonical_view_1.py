with open('../Individual_task/inputs/canonical_input_1.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/canonical_output_1.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    graph = {}
    for i in range(n):
        graph[i + 1] = 0
    for i in range(n):
        v = [int(i) for i in f_input.readline().split()]
        for j in range(n):
            if v[j] == 1:
                graph[j + 1] = i + 1
    for i in sorted(graph.keys()):
        print(graph[i], end=' ', file=f_output)
