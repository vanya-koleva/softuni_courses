namespace _07.TrekkingMania;

class Program
{
    static void Main(string[] args)
    {
        int groupsNum = int.Parse(Console.ReadLine());

        int musalaClimbers = 0;
        int montBlancClimbers = 0;
        int kilimanjaroClimbers = 0;
        int k2Climbers = 0;
        int everestClimbers = 0;
        int totalClimbers = 0;

        for (int group = 0; group < groupsNum; group++)
        {
            int persons = int.Parse(Console.ReadLine());
            
            if (persons <= 5) musalaClimbers += persons;
            else if (persons <= 12) montBlancClimbers += persons;
            else if (persons <= 25) kilimanjaroClimbers += persons;
            else if (persons <= 40) k2Climbers += persons;
            else everestClimbers += persons;
            
            totalClimbers += persons;
        }
        
        Console.WriteLine($"{(double)musalaClimbers / totalClimbers * 100:F2}%");
        Console.WriteLine($"{(double)montBlancClimbers / totalClimbers * 100:F2}%");
        Console.WriteLine($"{(double)kilimanjaroClimbers / totalClimbers * 100:F2}%");
        Console.WriteLine($"{(double)k2Climbers / totalClimbers * 100:F2}%");
        Console.WriteLine($"{(double)everestClimbers / totalClimbers * 100:F2}%");
    }
}