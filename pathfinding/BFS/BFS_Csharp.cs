using System;
using System.Collections.Generic;

public class Pathfinding
{
    public static bool IsValid(int[][] matrix, bool[][] visited, int x, int y)
    {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        return x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] == 0 && !visited[x][y];
    }

    public static bool BFS(int[][] matrix, int x1, int y1, int x2, int y2)
    {
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        bool[][] visited = new bool[rows][];
        for (int i = 0; i < rows; i++)
        {
            visited[i] = new bool[cols];
        }

        Queue<(int, int)> queue = new Queue<(int, int)>();
        queue.Enqueue((x1, y1));
        visited[x1][y1] = true;

        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();

            if (x == x2 && y == y2)
            {
                return true;
            }

            int[] dx = { -1, 1, 0, 0 };
            int[] dy = { 0, 0, -1, 1 };
            for (int i = 0; i < 4; i++)
            {
                int new_x = x + dx[i];
                int new_y = y + dy[i];

                if (IsValid(matrix, visited, new_x, new_y))
                {
                    queue.Enqueue((new_x, new_y));
                    visited[new_x][new_y] = true;
                }
            }
        }

        return false;
    }

    public static void Main(string[] args)
    {
        int[][] matrix = new int[][]
        {
            new int[] { 0, 0, 0, 0, 0, 0 },
            new int[] { 0, 0, 0, 1, 0, 0 },
            new int[] { 0, 0, 0, 0, 0, 0 },
            new int[] { 0, 0, 0, 0, 1, 0 },
            new int[] { 0, 0, 0, 0, 1, 0 },
            new int[] { 0, 0, 0, 0, 1, 0 },
            new int[] { 0, 0, 0, 1, 0, 0 }
        };

        int x1 = 0, y1 = 0; // Starting position
        int x2 = 6, y2 = 5; // Destination position

        bool result = BFS(matrix, x1, y1, x2, y2);
        Console.WriteLine(result);
    }
}
