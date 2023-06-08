using System;
using System.Collections.Generic;

class DFS_Csharp
{
    static List<(int, int)> DFS(int[,] matrix, int x1, int y1, int x2, int y2)
    {
        // Kiểm tra xem các tọa độ đầu vào có hợp lệ không
        if (!IsValid(matrix, x1, y1) || !IsValid(matrix, x2, y2))
        {
            return null;
        }

        // Khởi tạo stack để lưu trữ các nút cần duyệt
        var stack = new Stack<(int, int, List<(int, int)>)>();
        stack.Push((x1, y1, new List<(int, int)>()));

        while (stack.Count > 0)
        {
            var (x, y, path) = stack.Pop();

            // Kiểm tra xem đã đến vị trí đích chưa
            if (x == x2 && y == y2)
            {
                path.Add((x, y));
                return path;
            }

            // Kiểm tra xem ô hiện tại có thể di chuyển đến không
            if (IsValid(matrix, x, y) && matrix[x, y] == 0)
            {
                // Đánh dấu ô hiện tại đã được duyệt
                matrix[x, y] = -1;

                // Duyệt các ô lân cận (lên, xuống, trái, phải) trong ma trận
                int[,] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
                for (int i = 0; i < 4; i++)
                {
                    int nx = x + directions[i, 0];
                    int ny = y + directions[i, 1];

                    // Kiểm tra xem ô lân cận có hợp lệ và chưa được duyệt
                    if (IsValid(matrix, nx, ny) && matrix[nx, ny] == 0)
                    {
                        var newPath = new List<(int, int)>(path);
                        newPath.Add((x, y));
                        stack.Push((nx, ny, newPath));
                    }
                }
            }
        }

        // Không tìm thấy đường đi từ (x1, y1) đến (x2, y2)
        return null;
    }

    static bool IsValid(int[,] matrix, int x, int y)
    {
        // Kiểm tra xem tọa độ (x, y) có hợp lệ trong ma trận hay không
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }

    static void Main(string[] args)
    {
        int[,] matrix = {
            {0, 0, 0, 0, 0, 0},
            {0, 0, 0, 1, 0, 0},
            {0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 1, 0},
            {0, 0, 0, 0, 1, 0},
            {0, 0, 0, 0, 1, 0},
            {0, 0, 0, 1, 0, 0}
        };
        int x1 = 0, y1 = 0;
        int x2 = 6, y2 = 5;

        var result = DFS(matrix, x1, y1, x2, y2);

        if (result != null)
        {
            Console.WriteLine("Đường đi từ ({0}, {1}) đến ({2}, {3}):", x1, y1, x2, y2);
            for (int i = result.Count - 1; i >= 0; i--)
            {
                Console.WriteLine("({0}, {1})", result[i].Item1, result[i].Item2);
            }
        }
        else
        {
            Console.WriteLine("Không tìm thấy đường đi từ ({0}, {1}) đến ({2}, {3}).", x1, y1, x2, y2);
        }
    }
}
