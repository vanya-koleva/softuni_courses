namespace _05.Travelling;

class Program
{
    static void Main(string[] args)
    {
        string destination = Console.ReadLine();

        while (destination != "End")
        {
            double neededMoney = double.Parse(Console.ReadLine());
            double currentMoney = 0;

            while (currentMoney < neededMoney)
            {
                currentMoney += double.Parse(Console.ReadLine());
            }
            
            Console.WriteLine($"Going to {destination}!");
            destination = Console.ReadLine();
        }
    }
}