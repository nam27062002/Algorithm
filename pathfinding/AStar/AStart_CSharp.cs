using System;
using System.Collections.Generic;

public class AStarNode : IComparable<AStarNode>
{
    public int X { get; set; }
    public int Y { get; set; }
    public int DistanceFromStart { get; set; }
    public int HeuristicDistanceToEnd { get; set; }
    public int TotalDistance => DistanceFromStart + HeuristicDistanceToEnd;
    public AStarNode Previous { get; set; }

    public AStarNode(int x, int y)
    {
        X = x;
        Y = y;
        DistanceFromStart = int.MaxValue;
        HeuristicDistanceToEnd = 0;
        Previous = null;
    }

    public int CompareTo(AStarNode other)
    {
        return TotalDistance.CompareTo(other.TotalDistance);
    }
}

public class AStar
{
    public static List<(int, int)> FindPath(int[,] matrix, int x1, int y1, int x2, int y2)
    {
        if (!IsValid(matrix, x1, y1) || !IsValid(matrix, x2, y2))
            return null;

        var queue = new PriorityQueue<AStarNode>();
        var startNode = new AStarNode(x1, y1);
        startNode.DistanceFromStart = 0;
        queue.Enqueue(startNode);

        var distance = new int[matrix.GetLength(0), matrix.GetLength(1)];
        for (int i = 0; i < distance.GetLength(0); i++)
        {
            for (int j = 0; j < distance.GetLength(1); j++)
            {
                distance[i, j] = int.MaxValue;
            }
        }
        distance[x1, y1] = 0;

        var previous = new AStarNode[matrix.GetLength(0), matrix.GetLength(1)];

        while (queue.Count > 0)
        {
            var currentNode = queue.Dequeue();

            if (currentNode.X == x2 && currentNode.Y == y2)
                return ReconstructPath(previous, currentNode);

            foreach (var (dx, dy) in new (int, int)[] { (1, 0), (-1, 0), (0, 1), (0, -1) })
            {
                var nx = currentNode.X + dx;
                var ny = currentNode.Y + dy;

                if (IsValid(matrix, nx, ny) && matrix[nx, ny] == 0)
                {
                    var newDistance = distance[currentNode.X, currentNode.Y] + 1;

                    if (newDistance < distance[nx, ny])
                    {
                        distance[nx, ny] = newDistance;
                        var neighborNode = new AStarNode(nx, ny)
                        {
                            DistanceFromStart = newDistance,
                            HeuristicDistanceToEnd = Heuristic(nx, ny, x2, y2),
                            Previous = currentNode
                        };
                        queue.Enqueue(neighborNode);
                        previous[nx, ny] = currentNode;
                    }
                }
            }
        }

        return null;
    }

    public static bool IsValid(int[,] matrix, int x, int y)
    {
        int rows = matrix.GetLength(0);
        int cols = matrix.GetLength(1);
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }

    public static int Heuristic(int x1, int y1, int x2, int y2)
    {
        return Math.Abs(x1 - x2) + Math.Abs(y1 - y2);
    }

    public static List<(int, int)> ReconstructPath(AStarNode[,] previous, AStarNode node)
    {
        var path = new List<(int, int)>();
        while (node != null)
        {
            path.Add((node.X, node.Y));
            node = previous[node.X, node.Y];
        }
        path.Reverse();
        return path;
    }
}

public class PriorityQueue<T> where T : IComparable<T>
{
    private List<T> list;

    public int Count => list.Count;

    public PriorityQueue()
    {
        list = new List<T>();
    }

    public void Enqueue(T item)
    {
        list.Add(item);
        int childIndex = list.Count - 1;
        while (childIndex > 0)
        {
            int parentIndex = (childIndex - 1) / 2;
            if (list[childIndex].CompareTo(list[parentIndex]) >= 0)
                break;
            T tmp = list[childIndex];
            list[childIndex] = list[parentIndex];
            list[parentIndex] = tmp;
            childIndex = parentIndex;
        }
    }

    public T Dequeue()
    {
        int lastIndex = list.Count - 1;
        T frontItem = list[0];
        list[0] = list[lastIndex];
        list.RemoveAt(lastIndex);

        lastIndex--;
        int parentIndex = 0;
        while (true)
        {
            int leftChildIndex = parentIndex * 2 + 1;
            int rightChildIndex = parentIndex * 2 + 2;
            if (leftChildIndex > lastIndex)
                break;

            int childIndex = leftChildIndex;
            if (rightChildIndex <= lastIndex && list[rightChildIndex].CompareTo(list[leftChildIndex]) < 0)
                childIndex = rightChildIndex;

            if (list[parentIndex].CompareTo(list[childIndex]) <= 0)
                break;

            T tmp = list[parentIndex];
            list[parentIndex] = list[childIndex];
            list[childIndex] = tmp;
            parentIndex = childIndex;
        }

        return frontItem;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        int[,] matrix = {
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

        var result = AStar.FindPath(matrix, x1, y1, x2, y2);
        if (result != null)
        {
            foreach (var (x, y) in result)
            {
                Console.WriteLine($"({x}, {y})");
            }
        }
        else
        {
            Console.WriteLine("No path found.");
        }
    }
}
