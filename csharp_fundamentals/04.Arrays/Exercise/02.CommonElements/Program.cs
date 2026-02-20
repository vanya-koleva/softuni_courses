namespace _02.CommonElements;

class Program
{
    static void Main(string[] args)
    {
        string[] arr1 = Console.ReadLine().Split(' ');
        string[] arr2 = Console.ReadLine().Split(' ');

        string common = "";

        foreach (var el in arr2)
        {
            if (arr1.Contains(el))
            {
                common += el + " ";
            }
        }
        
        Console.WriteLine(common);
    }
}