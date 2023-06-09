#======================= Phần cũ ==============================
from collections import deque
import time
def is_valid(matrix, visited, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 0 and not visited[x][y]

def bfs(matrix, x1, y1, x2, y2):
    global is_finish,visited
    queue = deque([(x1, y1)])
    visited[x1][y1] = True
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            is_finish = True
            path = reconstruct_path(previous,x1,y1,x2,y2)
            visited = [[False] * cols for _ in range(rows)]
            for i in path:
                visited[i[0]][i[1]] = True
            return True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if is_valid(matrix, visited, new_x, new_y):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                previous[new_x][new_y] = (x, y)  # Lưu vị trí trước đó
                time.sleep(0.1)

    return False

def reconstruct_path(previous, x1, y1, x2, y2):
    path = [(x2, y2)]
    while (x2, y2) != (x1, y1):
        x2, y2 = previous[x2][y2]
        path.append((x2, y2))
    path.reverse()
    return path
#======================= Phần mới ==============================
import pygame
import threading

pygame.init()
WIDTH = 1000
HEIGHT = 600
RUNNING = True
is_finish = False
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BFS")
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]
x1, y1 = 0, 0  # Starting position
x2, y2 = 9, 18  # Destination position
rows = len(matrix) # số lượng hàng
cols = len(matrix[0]) # số lượng cột

size = min(WIDTH // cols,HEIGHT // rows)
dx = (WIDTH - size * cols) // 2
dy = (HEIGHT - size * rows) // 2
visited = [[False] * cols for _ in range(rows)]
previous = [[None] * cols for _ in range(rows)]
def draw_squares():
    for i in range(rows):
        for j in range(cols):
            if x1 == i and y1 == j or x2 == i and y2 == j:
                pygame.draw.rect(screen,(0,128,255),(dx + j *size,dy + i * size,size,size),0)
            elif matrix[i][j] == 1:
                pygame.draw.rect(screen,(255,255,0),(dx + j *size,dy + i * size,size,size),0)
            else: # cái này có thể đi được
                if visited[i][j]:
                    pygame.draw.rect(screen,(0,255,0),(dx + j *size,dy + i * size,size,size),0)
                else:
                    pygame.draw.rect(screen,(255,255,255),(dx + j *size,dy + i * size,size,size),0)
            pygame.draw.rect(screen,(0,0,0),(dx + j *size,dy + i * size,size,size),1)
            
t1 = threading.Thread(target=bfs,args=(matrix,x1,y1,x2,y2,))
t1.start()
while RUNNING:
    screen.fill((255,255,255))
    draw_squares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.display.update()
pygame.quit()    


