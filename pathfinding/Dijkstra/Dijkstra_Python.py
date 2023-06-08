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

result = dijkstra(matrix, x1, y1, x2, y2)
print(result)
