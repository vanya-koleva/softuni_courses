namespace _01.NumberPyramid;

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());

        int current = 1;
        bool isDone = false;

        for (int row = 1; row <= n; row++)
        {
            for (int col = 1; col <= row; col++)
            {
                Console.Write(current + " ");
                current++;
                if (current > n)
                {
                    isDone = true;
                    break;
                }
            }
            
            Console.WriteLine();
            if (isDone)
            {
                break;
            }
        }
    }
}