#======================= Phần cũ ==============================
import time
def is_valid(matrix, x, y):
    # Kiểm tra xem tọa độ (x, y) có hợp lệ trong ma trận hay không
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols

def dfs(matrix, x1, y1, x2, y2):
    # Kiểm tra xem các tọa độ đầu vào có hợp lệ không
    if not is_valid(matrix, x1, y1) or not is_valid(matrix, x2, y2):
        return None

    # Khởi tạo stack để lưu trữ các nút cần duyệt
    stack = [(x1, y1, [])]

    while stack:
        x, y, path = stack.pop()

        # Kiểm tra xem đã đến vị trí đích chưa
        if x == x2 and y == y2:
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] == -1:
                        matrix[i][j] = 0
            for i in path:
                if i[0] != x1 and i[1] != y1 or i[0] != x2 and i[1] != y2:
                    matrix[i[0]][i[1]] = -1
            return path + [(x, y)]

        # Kiểm tra xem ô hiện tại có thể di chuyển đến không
        if is_valid(matrix, x, y) and matrix[x][y] == 0:
            # Đánh dấu ô hiện tại đã được duyệt
            matrix[x][y] = -1

            # Duyệt các ô lân cận (lên, xuống, trái, phải) trong ma trận
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                # Kiểm tra xem ô lân cận có hợp lệ và chưa được duyệt
                if is_valid(matrix, nx, ny) and matrix[nx][ny] == 0:
                    stack.append((nx, ny, path + [(x, y)]))
        time.sleep(0.1)
    # Không tìm thấy đường đi từ (x1, y1) đến (x2, y2)
    return None


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

def draw_squares():
    for i in range(rows):
        for j in range(cols):
            if x1 == i and y1 == j or x2 == i and y2 == j:
                pygame.draw.rect(screen,(0,128,255),(dx + j *size,dy + i * size,size,size),0)
            elif matrix[i][j] == 1:
                pygame.draw.rect(screen,(255,255,0),(dx + j *size,dy + i * size,size,size),0)
            else: # cái này có thể đi được
                if matrix[i][j] == -1:
                    pygame.draw.rect(screen,(0,255,0),(dx + j *size,dy + i * size,size,size),0)
                else:
                    pygame.draw.rect(screen,(255,255,255),(dx + j *size,dy + i * size,size,size),0)
            pygame.draw.rect(screen,(0,0,0),(dx + j *size,dy + i * size,size,size),1)
            
t1 = threading.Thread(target=dfs,args=(matrix,x1,y1,x2,y2,))
t1.start()
while RUNNING:
    screen.fill((255,255,255))
    draw_squares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.display.update()
pygame.quit()    


