int size = int.Parse( Console.ReadLine());

PrintTriangle(size);

static void PrintLine(int start, int end)
{
    for (int i = start; i <= end; i++) 
    {
        Console.Write($"{i} ");
    }
    Console.WriteLine();
}

static void PrintFirstHalf(int n)
{
    for (int i = 1; i <= n; i++)
    {
        PrintLine(1, i);
    }
}

static void PrintSecondHalf(int n)
{
    for (int i = n - 1; i >= 1; i--)
    {
        PrintLine(1, i);
    }
}

static void PrintTriangle(int size) 
{
    PrintFirstHalf(size);
    PrintSecondHalf(size);
}