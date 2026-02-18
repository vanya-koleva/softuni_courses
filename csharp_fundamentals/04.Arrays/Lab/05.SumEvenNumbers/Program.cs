namespace _05.SumEvenNumbers;

class Program
{
    static void Main(string[] args)
    {
        int[] numbers = Console.ReadLine()
            .Split()
            .Select(int.Parse)
            .ToArray();
        
        int totalEven =  numbers.Sum(n => n % 2 == 0 ? n : 0);
        
        Console.WriteLine(totalEven);
    }
}