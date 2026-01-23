namespace _07.RepeatString;

class Program
{
    static void Main(string[] args)
    {
        string str = Console.ReadLine();
        int count = int.Parse(Console.ReadLine());
        
        Console.WriteLine(RepeatString(str, count));

        static string RepeatString(string text, int n)
        {
            return string.Concat(Enumerable.Repeat(text, n));
        }
    }
}