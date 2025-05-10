namespace _04.TrainTheTrainers;

class Program
{
    static void Main(string[] args)
    {
        int juryNumber = int.Parse(Console.ReadLine());
        
        int presentations = 0;
        double totalAverage = 0;

        while (true)
        {
            string presentation = Console.ReadLine();

            if (presentation == "Finish")
            {
                break;
            }

            double totalGrades = 0;

            for (int i = 0; i < juryNumber; i++)
            {
                double grade = double.Parse(Console.ReadLine());
                totalGrades += grade;
            }
            
            double average = totalGrades / juryNumber;
            totalAverage += average;
            presentations++;
            Console.WriteLine($"{presentation} - {average:F2}.");
        }
        
        Console.WriteLine($"Student's final assessment is {totalAverage / presentations:F2}.");
    }
}