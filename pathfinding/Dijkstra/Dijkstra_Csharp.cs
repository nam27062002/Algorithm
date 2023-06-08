using System;
using System.Collections.Generic;

namespace Pathfinding.Dijkstra
{
    public class Dijkstra
    {
        public static List<Tuple<int, int>> FindShortestPath(int[,] matrix, int x1, int y1, int x2, int y2)
        {
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);

            // Kiểm tra xem các tọa độ đầu vào có hợp lệ không
            if (!IsValid(matrix, x1, y1) || !IsValid(matrix, x2, y2))
                return null;

            // Khởi tạo mảng khoảng cách và đỉnh trước đó
            int[,] distance = new int[rows, cols];
            Tuple<int, int>[,] previous = new Tuple<int, int>[rows, cols];

            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    distance[i, j] = int.MaxValue;
                    previous[i, j] = null;
                }
            }

            // Đặt khoảng cách từ điểm xuất phát là 0
            distance[x1, y1] = 0;

            // Tạo hàng đợi ưu tiên để lưu trữ các đỉnh cần duyệt theo khoảng cách
            PriorityQueue<Tuple<int, int>> pq = new PriorityQueue<Tuple<int, int>>();
            pq.Enqueue(new Tuple<int, int>(x1, y1), 0);

            while (pq.Count > 0)
            {
                Tuple<int, int> current = pq.Dequeue();
                int x = current.Item1;
                int y = current.Item2;

                // Kiểm tra xem đã đến điểm đích chưa
                if (x == x2 && y == y2)
                {
                    List<Tuple<int, int>> path = new List<Tuple<int, int>>();
                    while (previous[x, y] != null)
                    {
                        path.Add(new Tuple<int, int>(x, y));
                        Tuple<int, int> prev = previous[x, y];
                        x = prev.Item1;
                        y = prev.Item2;
                    }
                    path.Reverse();
                    return path;
                }

                // Duyệt các ô lân cận (lên, xuống, trái, phải) trong ma trận
                int[] dx = { -1, 1, 0, 0 };
                int[] dy = { 0, 0, -1, 1 };
                for (int i = 0; i < 4; i++)
                {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    // Kiểm tra xem ô lân cận có hợp lệ và chưa được duyệt
                    if (IsValid(matrix, nx, ny) && matrix[nx, ny] == 0)
                    {
                        // Tính toán khoảng cách mới
                        int newDist = distance[x, y] + 1;

                        // Nếu khoảng cách mới nhỏ hơn khoảng cách hiện tại, cập nhật khoảng cách và đỉnh trước đó
                        if (newDist < distance[nx, ny])
                        {
                            distance[nx, ny] = newDist;
                            previous[nx, ny] = new Tuple<int, int>(x, y);
                            pq.Enqueue(new Tuple<int, int>(nx, ny), newDist);
                        }
                    }
                }
            }

            // Không tìm thấy đường đi từ (x1, y1) đến (x2, y2)
            return null;
        }

        private static bool IsValid(int[,] matrix, int x, int y)
        {
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            return x >= 0 && x < rows && y >= 0 && y < cols;
        }
    }

    public class PriorityQueue<T>
    {
        private List<Tuple<T, int>> elements;

        public int Count { get { return elements.Count; } }

        public PriorityQueue()
        {
            elements = new List<Tuple<T, int>>();
        }

        public void Enqueue(T item, int priority)
        {
            elements.Add(new Tuple<T, int>(item, priority));
        }

        public T Dequeue()
        {
            int bestIndex = 0;
            for (int i = 0; i < elements.Count; i++)
            {
                if (elements[i].Item2 < elements[bestIndex].Item2)
                    bestIndex = i;
            }

            T bestItem = elements[bestIndex].Item1;
            elements.RemoveAt(bestIndex);
            return bestItem;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int[,] matrix = new int[,]
            {
                { 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 1, 0 },
                { 0, 0, 0, 0, 1, 0 },
                { 0, 0, 0, 0, 1, 0 },
                { 0, 0, 0, 1, 0, 0 }
            };

            int x1 = 0, y1 = 0;
            int x2 = 6, y2 = 5;

            var result = Dijkstra.FindShortestPath(matrix, x1, y1, x2, y2);

            if (result != null)
            {
                Console.WriteLine("Shortest path:");
                foreach (var point in result)
                {
                    Console.WriteLine($"({point.Item1}, {point.Item2})");
                }
            }
            else
            {
                Console.WriteLine("No path found.");
            }

            Console.ReadLine();
        }
    }
}
