namespace _05.AccountBalance;

class Program
{
    static void Main(string[] args)
    {
        string command = Console.ReadLine();
        
        double total = 0;

        while (command != "NoMoreMoney")
        {
            double currentSum = double.Parse(command);

            if (currentSum < 0)
            {
                Console.WriteLine("Invalid operation!");
                break;
            }
            
            Console.WriteLine($"Increase: {currentSum:F2}");
            total += currentSum;
            
            command = Console.ReadLine();
        }
        
        Console.WriteLine($"Total: {total:F2}");
    }
}