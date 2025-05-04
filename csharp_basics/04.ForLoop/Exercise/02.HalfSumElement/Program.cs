namespace _02.HalfSumElement;

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        
        int sum = 0;
        int max = int.MinValue;
        
        for (int i = 1; i <= n; i++)
        {
            int num = int.Parse(Console.ReadLine());
            
            sum += num;

            if (max < num)
            {
                max = num;
            }
        }
        
        sum -= max;

        if (max == sum)
        {
            Console.WriteLine("Yes");
            Console.WriteLine($"Sum = {sum}");
        }
        else
        {
            Console.WriteLine("No");
            Console.WriteLine($"Diff = {Math.Abs(sum - max)}");
        }
    }
}