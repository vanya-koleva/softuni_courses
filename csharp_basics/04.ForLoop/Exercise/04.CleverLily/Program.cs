namespace _04.CleverLily;

class Program
{
    static void Main(string[] args)
    {
        int age = int.Parse(Console.ReadLine());
        double laundryPrice = double.Parse(Console.ReadLine());
        int pricePerToy = int.Parse(Console.ReadLine());

        int moneyIncrement = 10;
        int moneyDecrement = 1;
        
        int toysNum = 0;
        double totalSum = 0.0;

        for (int i = 1; i <= age; i++)
        {
            if (i % 2 == 0)
            {
                totalSum += moneyIncrement;
                totalSum -= moneyDecrement;
                moneyIncrement += 10;
            }
            else
            {
                toysNum++;
            }
        }
        
        totalSum += toysNum * pricePerToy;
        
        double diff = Math.Abs(laundryPrice - totalSum);

        if (totalSum >= laundryPrice)
        {
            Console.WriteLine($"Yes! {diff:F2}");
        }
        else
        {
            Console.WriteLine($"No! {diff:F2}");
        }
    }
}