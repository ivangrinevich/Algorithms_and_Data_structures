from array import array


with open('../Individual_task/inputs/task_2_input.txt', 'r', encoding='utf-8') as f_input, \
        open('../Individual_task/outputs/task_2_output.txt', 'w', encoding='utf-8') as f_output:
    s, n, m = [int(i) for i in f_input.readline().split()]
    W = n * m
    toys = [array('q', [0 for _ in range(W + 1)]) for _ in range(s)]
    kit = [[int(j) for j in f_input.readline().split()] for _ in range(s)]
    d, t = array('q', [i[0] for i in kit]), array('q', [j[1] for j in kit])
    del kit
    for i in range(s):
        for j in range(W + 1):
            if d[i] > j:
                toys[i][j] = toys[i - 1][j]
            else:
                toys[i][j] = max(toys[i - 1][j], toys[i - 1][j - d[i]] + t[i])
    order = array('I', [])
    j = W
    for i in range(s - 1, 0, -1):
        if toys[i][j] != toys[i - 1][j]:
            order.append(i + 1)
            j -= d[i]
    if j >= d[0]:
        order.append(1)
    print(len(order), file=f_output)
    print(*reversed(order), file=f_output)
