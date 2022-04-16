with open('../Individual_task/inputs/is_heap_input.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/is_heap_output.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    to_check = [int(i) for i in f_input.readline().split()]
    i = 0
    while 2 * i + 1 < n:
        if 2 * i + 2 < n:
            if to_check[i] > to_check[2 * i + 1] or to_check[i] > to_check[2 * i + 2]:
                print('No', file=f_output)
                exit()
        else:
            if to_check[i] > to_check[2 * i + 1]:
                print('No', file=f_output)
                exit()
        i += 1
    print('Yes', file=f_output)
