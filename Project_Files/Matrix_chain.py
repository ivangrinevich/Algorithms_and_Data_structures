
with open('../Individual_task/inputs/input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/output.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    chain = [f_input.readline().split() for _ in range(n)]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
