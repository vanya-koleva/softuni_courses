double budget = double.Parse(Console.ReadLine());
int statistsNum = int.Parse(Console.ReadLine());
double clothingPrice = double.Parse(Console.ReadLine());

double totalClothing = statistsNum * clothingPrice * (statistsNum > 150 ? 0.9 : 1.0);
double totalCost = budget * 0.1 + totalClothing;
double difference = Math.Abs(budget - totalCost);

if (budget >= totalCost)
{
    Console.WriteLine("Action!");
    Console.WriteLine($"Wingard starts filming with {difference:F2} leva left.");
}
else
{
    Console.WriteLine("Not enough money!");
    Console.WriteLine($"Wingard needs {difference:F2} leva more.");
}
