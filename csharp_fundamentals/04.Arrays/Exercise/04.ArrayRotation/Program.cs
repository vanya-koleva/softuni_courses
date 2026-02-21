namespace _04.ArrayRotation;

class Program
{
    static void Main(string[] args)
    {
        int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int rotations = int.Parse(Console.ReadLine());

        rotations %= arr.Length;
        
        int[] rotated = arr.Skip(rotations).Concat(arr.Take(rotations)).ToArray();
        
        Console.WriteLine(string.Join(" ", rotated));
    }
}