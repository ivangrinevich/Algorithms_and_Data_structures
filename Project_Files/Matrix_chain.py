with open('../Individual_task/inputs/input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/output.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    chain = [f_input.readline().split() for _ in range(n)]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        matrix[i][i + 1] = int(chain[i][0]) * int(chain[i][1]) * int(chain[i + 1][1])
    j = 0
    for p in range(1, n):
        for i in range(n - p):
            x = 2 ** 31
            j = i + p
            for k in range(i, j):
                matrix[i][j] = matrix[i][k] + matrix[k + 1][j] + int(chain[i][0]) * int(chain[k][1]) * int(chain[j][1])
                if x > matrix[i][j]:
                    x = matrix[i][j]
            matrix[i][j] = x
    f_output.write(str(matrix[0][n - 1]))
