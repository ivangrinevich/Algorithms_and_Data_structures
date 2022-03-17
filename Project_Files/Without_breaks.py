def upper_bound(arr, elem):
    left = 0
    right = len(arr)
    if arr:
        while left < right:
            middle = (left + right) // 2
            if elem < arr[middle]:
                right = middle
            else:
                left = middle + 1
        return left
    else:
        return 0


with open('../Individual_task/inputs/without_breaks.txt', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/without_breaks_out.txt', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    f = [int(i) for i in f_input.readline().split()]
    increasing = []
    m = set(f)
    if len(m) == 1:
        print(1, file=f_output)
    else:
        for i in f:
            index = upper_bound(increasing, i)
            if index < len(increasing):
                if increasing[index - 1] != i:
                    increasing[index] = i
            else:
                if len(increasing) == 0 or i > increasing[index - 1]:
                    increasing.append(i)
        print(len(increasing), file=f_output)
