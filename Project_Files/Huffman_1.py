with open('../Individual_task/inputs/huffman.in', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/huffman.out', 'w', encoding='utf-8') as f_output:
        n = int(f_input.readline())
        symbol_frequency = [int(i) for i in f_input.readline().split()]
        res = 0
        arr_1 = [0 for _ in range(n + 2)]
        arr_2 = [0 for _ in range(n + 2)]
        pos_1 = 0
        pos_2 = 0
        for i in range(n):
            arr_1[i] = symbol_frequency[i]
            arr_2[i] = 9223372036854775807 // 2
        arr_1[n] = 9223372036854775807 // 2
        arr_2[n] = 9223372036854775807 // 2
        arr_1[n + 1] = 9223372036854775807 // 2
        arr_2[n + 1] = 9223372036854775807 // 2
        for i in range(n - 1):
            if arr_1[pos_1] + arr_1[pos_1 + 1] <= arr_1[pos_1] + arr_2[pos_2] and arr_1[pos_1] + arr_1[pos_1 + 1] <= arr_2[pos_2] + arr_2[pos_2 + 1]:
                arr_2[i] = arr_1[pos_1] + arr_1[pos_1 + 1]
                pos_1 += 2
            elif arr_1[pos_1] + arr_2[pos_2] <= arr_1[pos_1] + arr_1[pos_1 + 1] and arr_1[pos_1] + arr_2[pos_2] <= arr_2[pos_2] + arr_2[pos_2 + 1]:
                arr_2[i] = arr_1[pos_1] + arr_2[pos_2]
                pos_2 += 1
                pos_1 += 1
            elif arr_2[pos_2] + arr_2[pos_2 + 1] <= arr_1[pos_1] + arr_1[pos_1 + 1] and arr_2[pos_2] + arr_2[pos_2 + 1] <= arr_1[pos_1] + arr_2[pos_2]:
                arr_2[i] = arr_2[pos_2] + arr_2[pos_2 + 1]
                pos_2 += 2
            res += arr_2[i]
        print(res, file=f_output)
