namespace _01.Train;

class Program
{
    static void Main(string[] args)
    {
        int numberOfWagons  = int.Parse(Console.ReadLine());
        
        int[] peopleInWagon = new int[numberOfWagons];
        int total = 0;

        for (int i = 0; i < numberOfWagons; i++)
        {
            peopleInWagon[i] = int.Parse(Console.ReadLine());
            total += peopleInWagon[i];
        }
        
        Console.WriteLine(string.Join(" ", peopleInWagon));
        Console.WriteLine(total);
    }
}