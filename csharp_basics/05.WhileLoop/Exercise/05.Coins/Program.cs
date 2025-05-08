namespace _05.Coins;

class Program
{
    static void Main(string[] args)
    {
        double change = double.Parse(Console.ReadLine());
        
        int sum = (int)(change * 100);
        int coins = 0;

        coins += sum / 200;
        sum %= 200;
        
        coins += sum / 100;
        sum %= 100;
        
        coins += sum / 50;
        sum %= 50;
        
        coins += sum / 20;
        sum %= 20;
        
        coins += sum / 10;
        sum %= 10;
        
        coins += sum / 5;
        sum %= 5;
        
        coins += sum /2;
        sum %= 2;
        
        coins += sum / 1;
        
        // int[] coinValues = { 200, 100, 50, 20, 10, 5, 2, 1 };
        //
        // foreach (int coin in coinValues)
        // {
        //     coins += sum / coin;
        //     sum %= coin;
        // }
        
        Console.WriteLine(coins);
    }
}