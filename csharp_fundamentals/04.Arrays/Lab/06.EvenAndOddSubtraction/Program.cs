namespace _06.EvenAndOddSubtraction;

class Program
{
    static void Main(string[] args)
    {
        int[] nums = Console.ReadLine()
            .Split()
            .Select(int.Parse)
            .ToArray();
        
        int evenSum = nums.Sum(n => n % 2 == 0 ? n : 0);
        int oddSum = nums.Sum(n => n % 2 != 0 ? n : 0);
        int difference = evenSum - oddSum;
        
        Console.WriteLine(difference);
    }
}