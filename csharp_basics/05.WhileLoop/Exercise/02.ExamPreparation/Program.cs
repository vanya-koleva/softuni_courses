namespace _02.ExamPreparation;

class Program
{
    static void Main(string[] args)
    {
        const int fail = 4;
        
        int allowedFails = int.Parse(Console.ReadLine());

        int solvedProblemsNum = 0;
        int failedTimes = 0;
        string lastProblem = "";
        double gradesSum = 0;
        bool isPassed = false;

        while (failedTimes < allowedFails)
        {
            string command = Console.ReadLine();

            if (command == "Enough")
            {
                isPassed = true;
                break;
            }
            
            int grade = int.Parse(Console.ReadLine());

            if (grade <= fail)
            {
                failedTimes++;
            }
            
            gradesSum += grade;
            solvedProblemsNum++;
            lastProblem = command;
        }

        if (isPassed)
        {
            Console.WriteLine($"Average score: {gradesSum / solvedProblemsNum:F2}");
            Console.WriteLine($"Number of problems: {solvedProblemsNum}");
            Console.WriteLine($"Last problem: {lastProblem}");
        }
        else
        {
            Console.WriteLine($"You need a break, {failedTimes} poor grades.");
        }
    }
}