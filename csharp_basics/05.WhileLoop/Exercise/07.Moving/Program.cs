namespace _07.Moving;

class Program
{
    static void Main(string[] args)
    {
        double width = double.Parse(Console.ReadLine());
        double length = double.Parse(Console.ReadLine());
        double height = double.Parse(Console.ReadLine());
        
        double availableSpace = width * length * height;

        while (availableSpace > 0)
        {
            var command = Console.ReadLine();

            if (command == "Done")
            {
                break;
            }
            
            availableSpace -= int.Parse(command);
        }

        if (availableSpace >= 0)
        {
            Console.WriteLine($"{availableSpace} Cubic meters left.");
        }
        else
        {
            Console.WriteLine($"No more free space! You need {Math.Abs(availableSpace)} Cubic meters more.");
        }
    }
}