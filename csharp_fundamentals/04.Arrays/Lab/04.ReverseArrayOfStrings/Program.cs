namespace _04.ReverseArrayOfStrings;

class Program
{
    static void Main(string[] args)
    {
        string[] words = Console.ReadLine().Split(" ");
        
        Console.WriteLine(string.Join(" ", words.Reverse()));
    }
}