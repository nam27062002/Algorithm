#======================= Phần cũ ==============================
import time
import heapq

def dijkstra(matrix, x1, y1, x2, y2):
    # Kiểm tra xem các tọa độ đầu vào có hợp lệ không
    if not is_valid(matrix, x1, y1) or not is_valid(matrix, x2, y2):
        return None
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Khởi tạo ma trận khoảng cách vô cùng
    distance = [[float('inf')] * cols for _ in range(rows)]
    # Khởi tạo ma trận đỉnh trước đó
    previous = [[None] * cols for _ in range(rows)]
    
    # Điểm xuất phát có khoảng cách bằng 0
    distance[x1][y1] = 0
    
    # Tạo hàng đợi ưu tiên để lưu trữ các đỉnh cần xét
    pq = [(0, (x1, y1))]
    
    while pq:
        time.sleep(0.1)
        # Lấy đỉnh có khoảng cách nhỏ nhất từ hàng đợi ưu tiên
        dist, (x, y) = heapq.heappop(pq)
        
        # Kiểm tra xem đã đến đích chưa
        if x == x2 and y == y2:
            # Truy vết đường đi từ đích về xuất phát
            path = []
            while x is not None and y is not None:
                path.append((x, y))
                if previous[x][y] is not None:
                    x, y = previous[x][y]
                else:
                    break
            path.reverse()
            return path
        
        # Kiểm tra xem đỉnh hiện tại có khoảng cách nhỏ hơn khoảng cách đã biết không
        if dist > distance[x][y]:
            continue
        
        # Duyệt các đỉnh lân cận (lên, xuống, trái, phải)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            # Kiểm tra xem đỉnh lân cận có hợp lệ và không phải chướng ngại vật
            if is_valid(matrix, nx, ny) and matrix[nx][ny] == 0:
                # Tính toán khoảng cách mới
                new_dist = dist + 1
                
                # Nếu khoảng cách mới nhỏ hơn khoảng cách hiện tại, cập nhật khoảng cách và đỉnh trước đó
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    previous[nx][ny] = (x, y)
                    heapq.heappush(pq, (new_dist, (nx, ny)))
    
    # Không tìm thấy đường đi từ (x1, y1) đến (x2, y2)
    return None

def is_valid(matrix, x, y):
    # Kiểm tra xem tọa độ (x, y) có hợp lệ trong ma trận hay không
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols


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
            
t1 = threading.Thread(target=dijkstra,args=(matrix,x1,y1,x2,y2,))
t1.start()
while RUNNING:
    screen.fill((255,255,255))
    draw_squares()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    pygame.display.update()
pygame.quit()    


