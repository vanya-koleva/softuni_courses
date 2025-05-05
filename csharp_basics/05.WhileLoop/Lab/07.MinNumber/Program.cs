namespace _07.MinNumber;

class Program
{
    static void Main(string[] args)
    {
        int min = int.MaxValue;

        while (true)
        {
            string command = Console.ReadLine();

            if (command == "Stop")
            {
                break;
            }
            
            int number = int.Parse(command);

            if (number < min)
            {
                min = number;
            }
        }
        
        Console.WriteLine(min);
    }
}