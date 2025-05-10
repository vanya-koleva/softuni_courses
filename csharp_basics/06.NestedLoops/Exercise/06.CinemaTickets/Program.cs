namespace _06.CinemaTickets;

class Program
{
    static void Main(string[] args)
    {
        var tickets = new Dictionary<string, int>
        {
            {"student", 0},
            {"standard", 0},
            {"kid", 0}
        };

        while (true)
        {
            string movie = Console.ReadLine();

            if (movie == "Finish")
            {
                break;
            }
            
            int capacity = int.Parse(Console.ReadLine());
            int soldTickets = 0;

            for (int i = 0; i < capacity; i++)
            {
                string ticket = Console.ReadLine();

                if (ticket == "End")
                {
                    break;
                }
                
                tickets[ticket]++;
                soldTickets++;
            }
            
            double fullPercent = (double)soldTickets / capacity * 100;
            Console.WriteLine($"{movie} - {fullPercent:F2}% full.");
        }
        
        int totalTickets = tickets.Values.Sum();
        double studentsPercent = (double)tickets["student"] / totalTickets * 100;
        double standardsPercent = (double)tickets["standard"] / totalTickets * 100;
        double kidsPercent = (double)tickets["kid"] / totalTickets * 100;
        
        Console.WriteLine($"Total tickets: {totalTickets}");
        Console.WriteLine($"{studentsPercent:F2}% student tickets.");
        Console.WriteLine($"{standardsPercent:F2}% standard tickets.");
        Console.WriteLine($"{kidsPercent:F2}% kids tickets.");
    }
}