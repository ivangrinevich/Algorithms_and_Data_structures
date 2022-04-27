with open('../Individual_task/inputs/matrix_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/matrix_output.txt', 'w', encoding='utf-8') as f_output:
    n, m = [int(i) for i in f_input.readline().split()]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        i, j = [int(k) for k in f_input.readline().split()]
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1
    for i in matrix:
        print(*i, file=f_output)
