namespace _06.MaxNumber;

class Program
{
    static void Main(string[] args)
    {
        string command = Console.ReadLine();
        
        int maxNumber = int.MinValue;

        while (command != "Stop")
        {
            int num = int.Parse(command);

            if (num > maxNumber)
            {
                maxNumber = num;
            }
            
            command = Console.ReadLine();
        }
        
        Console.WriteLine(maxNumber);
    }
}