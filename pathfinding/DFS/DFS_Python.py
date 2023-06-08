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

result = dfs(matrix, x1, y1, x2, y2)  
print(result) 
