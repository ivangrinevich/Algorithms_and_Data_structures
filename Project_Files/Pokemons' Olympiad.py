m, n = [int(i) for i in input().split()]
pokemon_heights = [int(i) for i in input().split()]
pedestal_heights = [int(i) for i in input().split()]
height_matrix = [[0 for j in range(n)] for i in range(m)]
height_matrix[0][0] = pedestal_heights[0] + pokemon_heights[0]
max_value = height_matrix[0][0]
for i in range(1, n):
    if pedestal_heights[i] + pokemon_heights[0] < max_value:
        height_matrix[0][i], max_value = pedestal_heights[i] + pokemon_heights[0], pedestal_heights[i] + pokemon_heights[0]
    else:
        height_matrix[0][i] = max_value
for i in range(1, m):
    max_value = float("inf")
    for j in range(i, n):
        if height_matrix[i-1][j-1] == -1:
            height_matrix[i][j] = -1
            continue
        if height_matrix[i - 1][j - 1] < pokemon_heights[i] + pedestal_heights[j] and pokemon_heights[i] + pedestal_heights[j] < max_value:
            max_value = pokemon_heights[i] + pedestal_heights[j]
            height_matrix[i][j] = max_value
        elif height_matrix[i - 1][j - 1] < pokemon_heights[i] + pedestal_heights[j]:
            height_matrix[i][j] = max_value
        elif i != j and height_matrix[i - 1][j - 1] > pokemon_heights[i] + pedestal_heights[j]:
            height_matrix[i][j] = max_value
        else:
            height_matrix[i][j] = -1
i = m - 1
j = n - 1
positions = []
while 0 <= i <= j:
    if height_matrix[i][j] == pokemon_heights[i] + pedestal_heights[j]:
        positions.append(j)
        i -= 1
        j -= 1
    else:
        j -= 1
if len(positions) == m:
    for i in sorted(positions):
        print(i + 1, end=' ')
else:
    print(-1)
