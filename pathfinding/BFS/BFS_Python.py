from collections import deque

def is_valid(matrix, visited, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0 and not visited[x][y]

def bfs(matrix, x1, y1, x2, y2):
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = [[False] * cols for _ in range(rows)]

    queue = deque([(x1, y1)])  # Create a queue and enqueue the starting position
    visited[x1][y1] = True  # Mark the starting position as visited
    while queue:
        x, y = queue.popleft()  # Dequeue a position from the queue
        if x == x2 and y == y2:  # If we have reached the destination, return True
            return True

        dx = [-1, 1, 0, 0]  # Offsets for adjacent positions
        dy = [0, 0, -1, 1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if is_valid(matrix, visited, new_x, new_y):  # Check if the new position is valid
                queue.append((new_x, new_y))  # Enqueue the new position
                visited[new_x][new_y] = True  # Mark the new position as visited
    return False  # If the destination is not reachable, return False

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0]
]
x1, y1 = 0, 0  # Starting position
x2, y2 = 6, 5  # Destination position

result = bfs(matrix, x1, y1, x2, y2)  # Call the BFS function
print(result)  # Print the result
