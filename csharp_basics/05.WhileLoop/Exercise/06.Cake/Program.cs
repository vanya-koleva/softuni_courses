namespace _06.Cake;

class Program
{
    static void Main(string[] args)
    {
        int pieces = int.Parse(Console.ReadLine()) * int.Parse(Console.ReadLine());

        while (pieces > 0)
        {
            string command = Console.ReadLine();

            if (command == "STOP")
            {
                break;
            }
            
            pieces -= int.Parse(command);
        }

        if (pieces <= 0)
        {
            Console.WriteLine($"No more cake left! You need {Math.Abs(pieces)} pieces more.");
        }
        else
        {
            Console.WriteLine($"{pieces} pieces are left.");
        }
    }
}