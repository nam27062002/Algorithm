from collections import deque

def is_valid(matrix, visited, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0 and not visited[x][y]

def bfs(matrix, x1, y1, x2, y2):
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = [[False] * cols for _ in range(rows)]
    previous = [[None] * cols for _ in range(rows)]

    queue = deque([(x1, y1)])
    visited[x1][y1] = True
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            return True,previous

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if is_valid(matrix, visited, new_x, new_y):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                previous[new_x][new_y] = (x, y)  # Lưu vị trí trước đó

    return False

def reconstruct_path(previous, x1, y1, x2, y2):
    path = [(x2, y2)]
    while (x2, y2) != (x1, y1):
        x2, y2 = previous[x2][y2]
        path.append((x2, y2))
    path.reverse()
    return path

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0]
]
x1, y1 = 0, 0
x2, y2 = 6, 5

result = bfs(matrix, x1, y1, x2, y2)
if result[0]:
    path = reconstruct_path(result[1], x1, y1, x2, y2)
    print("Path:", path)
else:
    print("No path found.")
