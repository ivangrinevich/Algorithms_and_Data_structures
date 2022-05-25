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
if m not in list(zip(*height_matrix))[m - 1]:
    print(-1)
else:
    positions = []
    j = m - 1
    i = n - 1
    k = 0
    while j >= 0:
        if height_matrix[i][j] == m - k:
            positions.append(i + 1)
            if j == 0:
                break
            l = i
            k += 1
            while pokemon_heights[j] + pedestal_heights[l] <= pokemon_heights[j - 1] + pedestal_heights[i - 1] or height_matrix[i - 1][j - 1] != m - k:
                i -= 1
            i -= 1
            j -= 1
        else:
            i -= 1
    print(*sorted(positions))
