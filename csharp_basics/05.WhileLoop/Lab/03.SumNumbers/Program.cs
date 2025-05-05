namespace _03.SumNumbers;

class Program
{
    static void Main(string[] args)
    {
        int targetNum = int.Parse(Console.ReadLine());
        
        int sum = 0;

        while (sum < targetNum) 
        {
            int number = int.Parse(Console.ReadLine());
            
            sum += number;
        }
        
        Console.WriteLine(sum);
    }
}