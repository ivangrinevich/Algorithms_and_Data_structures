from math import ceil, floor
from heapq import heappop, heappush, heapify
from decimal import Decimal as dec

max_heap = []
heapify(max_heap)
min_heap = []
heapify(min_heap)
line = [dec(i) for i in input().split()]
heappush(max_heap, -1 * line[0])
n = 1
for i in line[1::]:
    if i:
        if i >= -1 * max_heap[0]:
            heappush(min_heap, i)
            n = len(min_heap) + len(max_heap)
            if len(min_heap) > floor(n / 2):
                m = heappop(min_heap)
                heappush(max_heap, dec(-1 * m))
        else:
            heappush(max_heap, -1 * i)
            n = len(min_heap) + len(max_heap)
            if len(max_heap) > ceil(n / 2):
                m = heappop(max_heap)
                heappush(min_heap, dec(-1 * m))
    else:
        if n % 2:
            print(-1 * max_heap[0])
        else:
            k = dec((-1 * max_heap[0] + min_heap[0]) / 2)
            print(int(k) if k * 10 % 10 == 0 else k)
