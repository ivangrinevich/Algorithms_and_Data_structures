m, n = [int(i) for i in input().split()]
pokemon_heights = [int(i) for i in input().split()]
pedestal_heights = [int(i) for i in input().split()]
height_matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n - m + 1):
    height_matrix[i][0] = 1
for j in range(m - 1):
    for i in range(j + 1, n):
        for k in range(i, n):
            if pokemon_heights[j] + pedestal_heights[i - 1] < pokemon_heights[j + 1] + pedestal_heights[k]:
                height_matrix[k][j + 1] = max(height_matrix[i - 1][j] + 1, height_matrix[k][j + 1])
            else:
                height_matrix[k][j + 1] = max(height_matrix[k][j + 1], height_matrix[i - 1][j])
height_matrix = list(zip(*height_matrix))
if m not in height_matrix[m - 1]:
    print(-1)
else:
    positions = []
    i = m - 1
    j = n - 1
    k = 0
    while i >= 0:
        if height_matrix[i][j] == m - k:
            positions.append(j + 1)
            if i == 0:
                break
            l = j
            k += 1
            while pokemon_heights[i] + pedestal_heights[l] <= pokemon_heights[i - 1] + pedestal_heights[j - 1] or height_matrix[i - 1][j - 1] != m - k:
                j -= 1
            i -= 1
            j -= 1
        else:
            j -= 1
    print(*sorted(positions))
