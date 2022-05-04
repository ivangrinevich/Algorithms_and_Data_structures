def dfs(v, m):
    dominos[v] = True
    m += 1
    for j in vec[v]:
        if not dominos[j]:
            m = dfs(j, m)
    return m


with open('../Individual_task/inputs/domino_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/domino_output.txt', 'w', encoding='utf-8') as f_output:
    vec = []
    dominos = [False for _ in range(7)]
    n = int(f_input.readline())
    for i in range(7):
        vec.append([])
        dominos[i] = True
    for i in range(n):
        a, b = [int(i) for i in f_input.readline().split()]
        dominos[a], dominos[b] = False, False
        vec[a].append(b)
        vec[b].append(a)
    n = 0
    for i in range(7):
        if not dominos[i]:
            n += 1
    for i in range(7):
        if not dominos[i]:
            g = dfs(i, 0)
            break
    if n != g:
        print("No", file=f_output)
    else:
        flag = True
        for i in range(7):
            if len(vec[i]) % 2 != 0:
                flag = False
                break
        if flag:
            print("Yes", file=f_output)
        else:
            print("No", file=f_output)
