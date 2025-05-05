namespace _08.Graduation;

class Program
{
    static void Main(string[] args)
    {
        string name = Console.ReadLine();

        const double passingGrade = 4.00;

        int fails = 0;
        double totalGrades = 0;
        int currentClass = 1;

        while (true)
        {
            double grade = double.Parse(Console.ReadLine());

            if (grade < passingGrade)
            {
                fails++;
                if (fails > 1)
                {
                    Console.WriteLine($"{name} has been excluded at {currentClass} grade");
                    break;
                }
                
                continue;
            }
            
            totalGrades += grade;
            currentClass++;

            if (currentClass > 12)
            {
                double averageGrade = totalGrades / 12;
                Console.WriteLine($"{name} graduated. Average grade: {averageGrade:F2}");
                break;
            }
        }
    }
}