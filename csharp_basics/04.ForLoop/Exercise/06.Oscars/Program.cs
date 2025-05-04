namespace _06.Oscars
{
    class Program
    {
        static void Main(string[] args)
        {
            string actorName = Console.ReadLine();
            double academyPoints = double.Parse(Console.ReadLine());
            int judgeCount = int.Parse(Console.ReadLine());

            const double PointsNeeded = 1250.5;

            double currentPoints = academyPoints;

            for (int i = 0; i < judgeCount; i++)
            {
                string judgeName = Console.ReadLine();
                double judgePoints = double.Parse(Console.ReadLine());

                currentPoints += judgePoints * judgeName.Length / 2;

                if (currentPoints > PointsNeeded)
                {
                    Console.WriteLine($"Congratulations, {actorName} got a nominee for leading role with {currentPoints:F1}!");
                    return;
                }
            }

            double pointsNeededDifference = PointsNeeded - currentPoints;

            Console.WriteLine($"Sorry, {actorName} you need {pointsNeededDifference:F1} more!");
        }
    }
}