namespace _08.TennisRanklist;

class Program
{
    static void Main(string[] args)
    {
        int tournamentsNum = int.Parse(Console.ReadLine());
        int startingPoints = int.Parse(Console.ReadLine());

        int totalPoints = 0;
        int tournamentsWon = 0;

        for (int i = 0; i < tournamentsNum; i++)
        {
            string result = Console.ReadLine();

            if (result == "W")
            {
                tournamentsWon++;
                totalPoints += 2000;
            }
            else if (result == "F")
            {
                totalPoints += 1200;
            }
            else
            {
                totalPoints += 720;
            }
        }
        
        double percentWon = (double)tournamentsWon / tournamentsNum * 100;
        int averagePoints = totalPoints / tournamentsNum;
        totalPoints += startingPoints;
        
        Console.WriteLine($"Final points: {totalPoints}");
        Console.WriteLine($"Average points: {averagePoints}");
        Console.WriteLine($"{percentWon:F2}%");
    }
}