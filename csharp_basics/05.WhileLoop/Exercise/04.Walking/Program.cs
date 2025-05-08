namespace _04.Walking;

class Program
{
    static void Main(string[] args)
    {
        const int goal = 10000;
        
        int total = 0;

        while (total < goal)
        {
            string command = Console.ReadLine();

            if (command == "Going home")
            {
                int steps = int.Parse(Console.ReadLine());
                total += steps;
                break;
            }
            
            total += int.Parse(command);
        }
        
        int diff = Math.Abs(goal - total);

        if (total >= goal)
        {
            Console.WriteLine("Goal reached! Good job!");
            Console.WriteLine($"{diff} steps over the goal!");
        }
        else
        {
            Console.WriteLine($"{diff} more steps to reach goal.");
        }
    }
}