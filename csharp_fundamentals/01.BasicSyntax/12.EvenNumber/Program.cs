while (true)
{
    int n = int.Parse(Console.ReadLine());

    if (n % 2 == 0)
    {
        Console.Write($"The number is: {Math.Abs(n)}");
        break;
    }
    
    Console.WriteLine("Please write an even number.");
}