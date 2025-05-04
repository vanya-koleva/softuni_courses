namespace _05.Salary;

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        double salary = double.Parse(Console.ReadLine());

        const int facebookFee = 150;
        const int instagramFee = 100;
        const int redditFee = 50;
        
        double currentSalary = salary;

        for (int i = 1; i <= n; i++)
        {
            string tab = Console.ReadLine();

            if (tab == "Facebook")
            {
                currentSalary -= facebookFee;
            }
            else if (tab == "Instagram")
            {
                currentSalary -= instagramFee;
            }
            else if (tab == "Reddit")
            {
                currentSalary -= redditFee;
            }

            if (currentSalary <= 0)
            {
                Console.WriteLine("You have lost your salary.");
                return;
            }
        }
        
        Console.WriteLine((int)currentSalary);
    }
}