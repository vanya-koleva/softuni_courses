from collections import deque


n = int(input())
matrix = []
kate_pos = []

for i in range(n):
    row = [ch for ch in input()]
    if 'k' in row:
        kate_pos = [i, row.index('k')]
        row[kate_pos[1]] = ' '
    matrix.append(row)

rows = len(matrix)
cols = len(matrix[0])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def is_exit(r, c):
    return r == 0 or r == rows - 1 or c == 0 or c == cols - 1


def bfs(start_row, start_col):
    queue = deque([(start_row, start_col, 1)])  # (row, col, steps)
    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True
    max_moves = 0

    while queue:
        r, c, moves = queue.popleft()

        if is_exit(r, c):
            max_moves = max(max_moves, moves)

        for dr, dc in directions.values():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if matrix[nr][nc] == ' ' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, moves + 1))

    return max_moves


start_r, start_c = kate_pos
max_path = bfs(start_r, start_c)

if max_path > 0:
    print(f'Kate got out in {max_path} moves')
else:
    print("Kate cannot get out")
