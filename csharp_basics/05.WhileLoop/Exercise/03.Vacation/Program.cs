namespace _03.Vacation;

class Program
{
    static void Main(string[] args)
    {
        const int maxSpendingDays = 5;
        
        double neededMoney = double.Parse(Console.ReadLine());
        double availableMoney = double.Parse(Console.ReadLine());
        
        int daysCounter = 0;
        int spendingDaysCounter = 0;

        while (neededMoney > availableMoney)
        {
            string action = Console.ReadLine();
            double sum = double.Parse(Console.ReadLine());
            
            daysCounter++;

            if (action == "spend")
            {
                availableMoney -= sum;
                availableMoney = Math.Max(availableMoney, 0);
                spendingDaysCounter++;

                if (spendingDaysCounter == maxSpendingDays)
                {
                    Console.WriteLine($"You can't save the money.");
                    Console.WriteLine(daysCounter);
                    break;
                }
            }
            else
            {
                availableMoney += sum;
                spendingDaysCounter = 0;
            }
        }

        if (availableMoney >= neededMoney)
        {
            Console.WriteLine($"You saved the money for {daysCounter} days.");
        }
    }
}