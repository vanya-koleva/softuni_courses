namespace _03.Zig_ZagArrays;

class Program
{
    static void Main(string[] args)
    {
        int numLines = int.Parse(Console.ReadLine());
        int[] arr1 = new int[numLines];
        int[] arr2 = new int[numLines];

        for (int i = 0; i < numLines; i++)
        {
            int[] currentLine = Console.ReadLine().Split().Select(int.Parse).ToArray();
            
            if ((i + 1)% 2 != 0)
            {
                arr1[i] = currentLine[0];
                arr2[i] = currentLine[1];
            }
            else
            {
                arr1[i] = currentLine[1];
                arr2[i] = currentLine[0];
            }
        }
        
        Console.WriteLine(string.Join(" ", arr1));
        Console.WriteLine(string.Join(" ", arr2));
    }
}