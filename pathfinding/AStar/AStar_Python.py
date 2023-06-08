import heapq

def AStar(matrix, x1, y1, x2, y2):
    # Kiểm tra xem các tọa độ đầu vào có hợp lệ không
    if not is_valid(matrix, x1, y1) or not is_valid(matrix, x2, y2):
        return None

    # Khởi tạo hàng đợi ưu tiên để lưu trữ các đỉnh cần duyệt theo ước lượng khoảng cách
    queue = []
    heapq.heappush(queue, (0, (x1, y1)))  # (ước lượng khoảng cách, (x, y))

    # Khởi tạo mảng khoảng cách từ điểm xuất phát
    distance = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
    distance[x1][y1] = 0

    # Khởi tạo mảng đỉnh trước đó để lưu trữ đường đi
    previous = [[None] * len(matrix[0]) for _ in range(len(matrix))]

    while queue:
        _, (x, y) = heapq.heappop(queue)

        # Kiểm tra xem đã đến điểm đích chưa
        if x == x2 and y == y2:
            return reconstruct_path(previous, x2, y2)

        # Duyệt các ô lân cận (lên, xuống, trái, phải) trong ma trận
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            # Kiểm tra xem ô lân cận có hợp lệ và không là chướng ngại vật
            if is_valid(matrix, nx, ny) and matrix[nx][ny] == 0:
                # Tính toán khoảng cách từ điểm xuất phát đến ô lân cận
                new_dist = distance[x][y] + 1

                # Nếu khoảng cách mới nhỏ hơn khoảng cách hiện tại, cập nhật khoảng cách và đỉnh trước đó
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    previous[nx][ny] = (x, y)
                    heapq.heappush(queue, (new_dist + heuristic(nx, ny, x2, y2), (nx, ny)))

    # Không tìm thấy đường đi từ (x1, y1) đến (x2, y2)
    return None

def is_valid(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols

def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(previous, x, y):
    path = []
    while previous[x][y] is not None:
        path.append((x, y))
        x, y = previous[x][y]
    path.append((x, y))
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

result = AStar(matrix, x1, y1, x2, y2)
print(result)
