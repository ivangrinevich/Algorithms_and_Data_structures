from heapq import *


with open('../Individual_task/inputs/huffman.in', 'r', encoding='utf-8') as f_input, \
     open('../Individual_task/outputs/huffman.out', 'w', encoding='utf-8') as f_output:
    n = int(f_input.readline())
    symbol_frequency = [int(i) for i in f_input.readline().split()]
    heapify(symbol_frequency)
    totals = []
    while len(symbol_frequency) != 1:
        one = heappop(symbol_frequency)
        two = heappop(symbol_frequency)
        total = one + two
        totals.append(total)
        heappush(symbol_frequency, total)
    print(sum(totals), file=f_output)
